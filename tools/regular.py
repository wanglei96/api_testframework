#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
正则相关操作类
"""
import re
import typing as t
from string import Template

from jsonpath_ng import parse

from tools.cache import cache
from tools.json_test import is_json_str
from tools.Logger import log


def findalls(string: t.Text) -> t.Dict[t.Text, t.Any]:
    """查找所有"""
    key = re.compile(r"\${(.*?)\}").findall(string)
    res = {k: cache.get(k) for k in key}
    log.debug("需要替换的变量：{}".format(res))
    return res


def sub_var(keys: t.Dict, string: t.Text) -> t.Text:
    """替换变量"""
    res = Template(string).safe_substitute(keys)
    log.debug("替换结果：{}".format(res))
    return res


def get_var(key: t.Text, raw_str: t.Text) -> t.Text:
    """获取变量"""
    if is_json_str(raw_str):
        return re.compile(r'\"%s":"(.*?)"' % key).findall(raw_str)[0]
    return re.compile(r'%s' % key).findall(raw_str)[0]


def filter_dict(regular, dict_data, keyword=None):
    """
    :param regular: 正则表达式
    :param dict_data: 传入多层嵌套的字典
    :param keyword: 根据正则返回的数据，通过关键字过滤
    :desc: jsonpath案例： https://blog.csdn.net/ToBeMaybe_/article/details/109495151
    :desc: jsonpath_ng用法： https://cloud.tencent.com/developer/article/1972066
    :return:
    """
    data = None
    # 根据正则提取字典的数据
    parser = parse(regular)
    # 根据keyword过滤数据并返回
    if keyword is not None:
        data = parser.filter(lambda x: x == keyword, dict_data)
    return data
