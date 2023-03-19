#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/28 17:48
# @Author  : 王磊
# @File    : test_demo.py
# @Software: PyCharm
import allure
import pytest

from api_object.api_demo import ApiDemo
from conftest import TEST_DATA
from const import TEST_DATA_PATH
from tools.yaml_driver import YamlDriver


@allure.feature('模块')
class TestDemo:

    @allure.story('模块-功能点')
    @pytest.mark.parametrize('role_code', TEST_DATA['demo']['role_code'], ids=TEST_DATA['demo']['ids'])
    def test_demo1(self, role_code):
        ApiDemo().get_user_by_role(role_code)

