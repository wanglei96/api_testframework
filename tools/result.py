import re
import time
import typing as t

import jmespath
import pytest
import allure
from requests import Response

from tools.Assertions import Assertions
from tools.cache import cache
from tools.Logger import logger
from tools.regular import get_var
from tools.utils import date_str_change_timestamp


def resp_report(r):
    allure.attach(name='请求URL', body=str(r.url))
    allure.attach(name='实际headers', body=str(r.headers))
    allure.attach(name='请求方式', body=str(r.request.method))
    allure.attach(name='请求内容', body=str(r.request.body))
    allure.attach(name='实际响应码', body=str(r.status_code))
    allure.attach(name='实际响应内容', body=r.text)


def get_result(r: Response, extract: t.List) -> None:
    """获取值"""
    for key in extract:
        value = get_var(key, r.text)
        logger.info("正则提取结果值：{}={}".format(key, value))
        cache.set(key, value)
        pytest.assume(key in cache)
    with allure.step("提取返回结果中的值"):
        for key in extract:
            allure.attach(name="提取%s" % key, body=cache.get(key))


def check_results(r: Response, validate: t.Dict) -> None:
    """检查运行结果"""
    """
        list_result_check格式: [[xx,xx,xx], key, value]  key,value表示需要遍历的key, value
    """
    expect_code = validate.get('expect_code')
    result_check = validate.get('result_check')
    check_json = validate.get('check_json')
    list_result_check = validate.get('list_result_check')
    regular_check = validate.get('regular_check')
    jmespath_check_json = validate.get('jmespath_check_json')

    if expect_code:
        with allure.step("校验返回响应码"):
            assert expect_code == r.status_code, resp_report(r)

    if result_check:
        with allure.step("校验响应预期值"):
            assert result_check in r.text, resp_report(r)

    if check_json:
        with allure.step("校验json数据"):
            assert check_json(check_json, r.json()), resp_report(r)

    if regular_check:
        with allure.step("正则校验返回结果"):
            assert re.findall(regular_check, r.text), resp_report(r)

    if jmespath_check_json:
        with allure.step("校验json数据"):
            for k, v in jmespath_check_json.items():
                if v[1] == 'equal':
                    Assertions.equal(v[0], jmespath.search(k, r.json()), resp_report(r))
                if v[1] == 'value_in':
                    Assertions.value_in(v[0], jmespath.search(k, r.json()), resp_report(r))
                if v[1] == 'not_equal':
                    Assertions.not_equal(v[0], jmespath.search(k, r.json()), resp_report(r))
                if v[1] == 'value_not_in':
                    Assertions.value_not_in(v[0], jmespath.search(k, r.json()), resp_report(r))
                if v[1] == 'values_in':
                    Assertions.values_in(v[0], jmespath.search(k, r.json()), resp_report(r))
                if v[1] == 'equals':
                    Assertions.equals(v[0], jmespath.search(k, r.json()), resp_report(r))


def check_socket_result(ws: t.Any, event: t.Text, condition_data: t.Dict, expect_data: t.Dict, fail_data=None,
                        timeout=3600):
    """
    断言websocket返回信息
    :param ws: websocket对象
    :param event: 事件名称
    :param condition_data: 判断哪一条信息是我们想要的
    :param expect_data: 预期结果
    :param fail_data: 失败状态参数
    :param timeout: 超时时间
    :return:
    """

    # 开始时间
    if fail_data is None:
        fail_data = {}
    start = time.time()
    while True:
        # 结束时间
        end = time.time()
        if end - start > timeout:
            break
        else:
            # 接受信息
            msg = ws.rev_msg()
            logger.info("msg:{}".format(msg))
            if msg['event'] == event:
                condition_keys = list(condition_data.keys())
                if msg['data'][condition_keys[0]] == condition_data[condition_keys[0]]:
                    expect_keys = expect_data.keys()
                    fail_keys = list(fail_data.keys())
                    for expect_key in expect_keys:
                        if msg['data'][expect_key] == expect_data[expect_key]:
                            ws.close()
                            return True
                        elif fail_data:
                            if msg['data'][expect_key] == fail_data[fail_keys[0]]:
                                ws.close()
                                return False
    ws.close()


def check_respone_key_value(data, key, *expect_value):
    result = False

    for item in data:
        for value in expect_value:
            if item[key] == value:
                result = True
                break
        assert result


def check_contain_value(data, key, *expect_value):
    for item in data:
        for value in expect_value:
            print(item[key])
            if value in item[key]:
                assert True
            else:
                assert False


def check_contain_time_range(data, key, start_time=None, end_time=None):
    for item in data:
        create_time = date_str_change_timestamp(item[key]) * 1000
        if start_time and end_time:
            if (start_time <= create_time) and (end_time >= create_time):
                assert True
            else:
                assert False
        elif not start_time:
            print(create_time, end_time)
            if end_time >= create_time:
                assert True
            else:
                assert False
        elif not end_time:
            if start_time <= create_time:
                assert True
            else:
                assert False
