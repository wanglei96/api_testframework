#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: 张福强
# datetime:2022/3/13 12:10 下午
# software: PyCharm

import pytest
import os

# from control_api.control_base import delete_all_data
from api_base.base_http import HttpRequest
from const import CONFIG_PATH, TEST_DATA_PATH
from tools.cache import cache
# from tools.base_http import HttpRequest
from tools.env_instance import EnvInstance

from tools.Logger import log

import deepwisdom

from tools.yaml_driver import YamlDriver

"""
    安装deepwisdom： pip install deepwisdom -i https://pypi.deepwisdomai.com/root/dev
"""


@pytest.fixture(scope="session", autouse=True)
def env(request):
    key_env = request.config.getoption('environment')
    YamlDriver(f'{CONFIG_PATH}config.yaml').set_value('env', key_env)
    return EnvInstance(key_env).create()


def pytest_addoption(parser):
    parser.addoption("--env",
                     action="store",
                     dest="environment",
                     default="test",
                     help="environment: test or prod")


@pytest.fixture(scope="session")
def logger():
    return log


@pytest.fixture(scope="session")
def common_client(env, logger):
    http = HttpRequest(env)

    # 登录系统
    # login.login_sys(env, logger)

    # 清除所有数据
    # delete_all_data(http, logger)

    yield http


"""
    SDK实例
"""


@pytest.fixture(scope="session")
def dw(env):
    api_client = deepwisdom.Client(appid=11, api_key="A9DzOEfZHZrNw00ATVakRSt5",
                                   secret_key="7S47E9yxXGOUhVikFgGnvlT3tcxrwLqc", domain="http://172.16.0.15:30997",
                                   admin_domain="https://tianji-admin.test.deepwisdomai.com")
    deepwisdom.set_client(client=api_client)
    yield deepwisdom

    """
        删除所有数据（虽然全局删除了，但是删除接口的异常case没有验证）
    """

    # 删除所有服务
    svc_ids: dict = cache.get("svc_ids")
    dw.Deployment.delete_deployments(svc_ids.values())

    # 删除所有离线预测
    offline_ids: dict = cache.get("offline_ids")
    dw.OfflinePrediction.delete_predictions(offline_ids.values())

    # 删除所有数据集
    dataset_ids: dict = cache.get("dataset_ids")
    dw.Dataset.delete(dataset_ids.values())

    # 删除所有项目
    project_ids: dict = cache.get("project_ids")
    dw.Project.delete(project_ids.values())


TEST_DATA = YamlDriver(TEST_DATA_PATH+'test_data.yaml').get_all_data()