#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @description: 接口参数模板
# @Time    : 2022/11/25 15:36
# @Author  : 王磊
# @File    : kwargs_model.py
# @Software: PyCharm

class KwargsModel:
    def __init__(self):
        """
        :param method: 发送方法
        :param route: 发送路径
        :param RequestData: request 请求参数
        :param Validate: 结果校验
        :param extract: 要提取的值
        :param Exception: 异常类型
        """
        self.method = ''
        self.route = ''
        self.RequestData = RequestData()
        self.Validate = Validate()
        self.extract = []
        self.Exception = ''

    def keys(self):
        return 'method', 'route', 'RequestData', 'Validate', 'extract', 'Exception'

    def __getitem__(self, item):
        return getattr(self, item)


class RequestData:
    def __init__(self):
        """
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
        """
        self.params = {}
        self.data = {}
        self.json = {}
        self.headers = {}
        self.cookies = {}
        self.files = ''
        self.timeout = ''
        self.auth = ''
        self.allow_redirects = ''
        self.proxies = ''
        self.stream = ''
        self.verify = ''
        self.cert = ''

    def keys(self):
        return 'params', 'data', 'json', \
               'headers', 'cookies', 'files', 'timeout', 'auth', 'allow_redirects', \
               'proxies', 'stream', 'verify', 'cert'

    def __getitem__(self, item):
        return getattr(self, item)


class Validate:
    """
    :param expect_code: 校验响应码
    :param result_check: 校验预期值在响应文本中
    :param check_json: 校验json数据
    :param jmespath_check_json: 使用jmespath进行json数据校验，填写方式：{“校验值的jmespath”: [预期值, 断言类型]， ...}
    可选的断言类型有：equal、value_in、not_equal、equals、value_not_in、values_in，参考tools中Assertions.py、result.py
    jmespath语法参考：https://cloud.tencent.com/developer/article/1784138
    https://jmespath.org/tutorial.html#basic-expressions
    示例：
    res_json = {"a": {"b": {"c": [{"d": [0, [1, 2]]}, {"d": [3, 4]}]}}}
    jmespath_check_json = {'a.b.c[0].d[1][0]': 1}
    :param regular_check: 正则校验返回结果
    """
    def __init__(self):
        self.expect_code = ''
        self.result_check = ''
        self.check_json = ''
        self.jmespath_check_json = {}
        self.regular_check = ''

    def keys(self):
        return 'expect_code', 'result_check', 'check_json', 'jmespath_check_json', 'regular_check'

    def __getitem__(self, item):
        return getattr(self, item)


if __name__ == "__main__":
    pass
    """
    使用示例：
    """
    KwargsModel = KwargsModel()

    KwargsModel.method = 'post'
    KwargsModel.route = '/login'
    KwargsModel.RequestData.data = {'username': 'xl', 'key': ''}
    KwargsModel.Validate.jmespath_check_json = {'a.b[0][0]': [110, 'equal']}

    #
    from api_base.base_http import HttpRequest

    print(HttpRequest().built_dict(KwargsModel))
