"""
序列化和反序列化类
"""
import json
import typing as t


def loads(content: t.Text) -> t.Any:
    """
    反序列化
        json对象 -> python数据类型
    """
    return json.loads(content)


def dumps(content: t.Union[t.Dict, t.List], ensure_ascii: bool = True) -> t.Text:
    """
    序列化
        python数据类型 -> json对象
    """
    return json.dumps(content, ensure_ascii=ensure_ascii)


def is_json_str(string: t.Text) -> bool:
    """验证是否为json字符串"""
    try:
        json.loads(string)
        return True
    except:
        return False


def check_json(check_data, resp_data):
    """
    校验的json
    :param check_data: 检验内容
    :param resp_data: 接口返回的数据
    :return:
    """
    flag = True
    if isinstance(check_data, dict):
        for key in check_data:
            if key not in resp_data:
                flag = False
            else:
                this_key = key
                if isinstance(check_data[this_key], dict) and isinstance(resp_data[this_key], dict):
                    check_json(check_data[this_key], resp_data[this_key])
                elif not isinstance(check_data[this_key], type(resp_data[this_key])):
                    flag = False
    else:
        raise Exception("JSON校验内容非dict格式：{}".format(check_data))
    return flag
