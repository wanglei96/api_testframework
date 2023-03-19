#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @description: 接口示例
# @Time    : 2022/11/28 15:12
# @Author  : 王磊
# @File    : api_demo.py
# @Software: PyCharm
from api_base.base_http import HttpRequest
from config.routes import demo_route
from tools.result import check_results


class ApiDemo(HttpRequest):

    def get_user(self, pageIndex, role_code='', username=''):
        """
        获取用户列表
        :param pageIndex: 页码
        :param role_code: 角色
        :param username: 人员名称
        :return:
        """
        # 填写请求参数
        self._request_model.method = 'post'
        self._request_model.route = demo_route
        self._request_model.RequestData.json = {
            "pageIndex": pageIndex,
            "role_code": role_code,
            "username": username
        }
        self._request_model.Validate.expect_code = 200
        self._request_model.Validate.jmespath_check_json = {
            "message": ["success!", 'equal'],

        }
        # 发起请求
        resp = self.send_request(self.built_dict(self._request_model))
        return resp

    def get_user_by_role(self, role_code):
        """
        通过角色码获取用户列表
        :param role_code:
        :return:
        """
        resp = self.get_user(1, role_code=role_code)
        validate = self._request_model.Validate
        validate.jmespath_check_json = {
            "data.user_data[].role_code": [role_code, 'equals']
        }
        check_results(resp, self.built_dict(validate))
        return resp.json()


if __name__ == "__main__":
    # ApiDemo().get_user(1)
    ApiDemo().get_user_by_role('ET')