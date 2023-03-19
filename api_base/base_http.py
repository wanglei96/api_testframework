"""
requests二次封装类
"""
import typing as t
from types import NoneType

import urllib3
from requests import Session, Response

from api_base.kwargs_model import KwargsModel
from const import ROOT_PATH, CONFIG_PATH
from tools.Logger import log
from tools.yaml_driver import YamlDriver
from tools.result import check_results, get_result


urllib3.disable_warnings()


class HttpRequest(Session):
    """requests方法二次封装"""

    def __init__(self, config_instance: YamlDriver = None):
        super(HttpRequest, self).__init__()
        self.config = config_instance
        self.global_config = YamlDriver(CONFIG_PATH+'config.yaml')
        if self.config is None:
            self.env = self.global_config.get_value('env')
            self.config = YamlDriver(ROOT_PATH+f'/config/{self.env}/config.yaml')
        self.need_log = self.config.get_base_config("need_log")
        self.logger = log
        self._request_model = KwargsModel()

    def send_request(self, kwargs: dict) -> Response:
        """发送请求
        :param method: 发送方法
        :param route: 发送路径
        optional 可选参数
        :param extract: 要提取的值
        :param params: 发送参数-"GET"
        :param data: 发送表单-"POST"
        :param json: 发送json-"post"
        :param headers: 头文件
        :param cookies: 验证字典
        :param files: 上传文件,字典：类似文件的对象``
        :param timeout: 等待服务器发送的时间
        :param auth: 基本/摘要/自定义HTTP身份验证
        :param allow_redirects: 允许重定向，默认为True
        :type bool
        :param proxies: 字典映射协议或协议和代理URL的主机名。
        :param stream: 是否立即下载响应内容。默认为“False”。
        :type bool
        :param verify: （可选）一个布尔值，在这种情况下，它控制是否验证服务器的TLS证书或字符串，在这种情况下，它必须是路径到一个CA包使用。默认为“True”。
        :type bool
        :param cert: 如果是字符串，则为ssl客户端证书文件（.pem）的路径
        :param exception: 异常类型
        :type Exception
        :return: request响应
        """
        headers = {}
        # 获取全局接口权限配置
        global_auth = self.global_config.get_value('global_auth')
        # key的值可以是cookie、token，根据项目决定
        auth_key = global_auth.get('key')
        auth_value = global_auth.get('value')
        if auth_key is not None and auth_value is not None:
            headers[auth_key] = auth_value
        exception = kwargs.get("exception", Exception)
        try:
            method = kwargs.get('method', 'GET').upper()
            domain = self.config.get_base_info('url')
            route = kwargs.get('route', '/')
            url = domain + route
            if ('http' or 'https') in route:
                url = route

            # 如果是上传文件的话，就不做变量替换，因为file文件传递过来的是二进制文件，再dumps会出错
            # if "files" not in kwargs.get('RequestData').keys():
            #     kwargs_str = dumps(kwargs)
            #     is_sub = findalls(kwargs_str)
            #     if is_sub:
            #         kwargs = loads(sub_var(is_sub, kwargs_str))

            # RequestData处理
            # params = {"bcode": "autotable", "token": "Hy+b55u4C9KE8GSKEJ5xhw=="}
            # if kwargs["RequestData"].get('params') is not None:
            #     kwargs["RequestData"]["params"].update(params)
            # else:
            #     kwargs["RequestData"]["params"] = params

            self.logger.info("Request Data: {}".format(kwargs))

            if kwargs["RequestData"].get('headers') is None:
                kwargs["RequestData"]["headers"] = headers

            response = self.dispatch(method, url, **kwargs.get('RequestData'))
            if self.need_log:
                self.logger.info("Response Result: {}".format(response.text.encode('utf-8').decode(encoding='unicode_escape')))
                self.logger.info("status_code: {}".format(response.status_code))

            # allure.attach("响应内容:{}".format(response.text), allure.attachment_type.TEXT)
            self.response_handle(response, kwargs.get('Validate'), kwargs.get('Extract', []))
            return response
        except exception as e:
            raise e

    def dispatch(self, method: t.Text, *args: t.Union[t.List, t.Tuple], **kwargs: t.Dict) -> Response:
        """请求分发"""
        handler = getattr(self, method.lower())
        return handler(*args, **kwargs)

    @staticmethod
    def mergedict(args: t.Dict, **kwargs: t.Dict) -> t.Dict:
        """合并字典"""
        for k, v in args.items():
            if k in kwargs:
                kwargs[k] = {**args[k], **kwargs.pop(k)}
        args.update(kwargs)
        return args

    def response_handle(self, r: Response, validate: t.Dict, extract: t.List):
        if validate:
            check_results(r, validate)
        if extract:
            get_result(r, extract)

    def built_dict(self, target):
        """
        转换实例为字典并过滤空键值对
        :param target: 实例对象，如KwargsModel()
        :return:
        """
        # obj_dict = copy.deepcopy(target.__dict__)
        obj_dict = {}
        for k, v in target.__dict__.items():
            if v:
                obj_dict[k] = v
                if type(v) not in [str, int, tuple, set, dict, list, NoneType, bool, float]:
                    obj_dict[k] = self.built_dict(v)
        return obj_dict


if __name__ == '__main__':
    pass
