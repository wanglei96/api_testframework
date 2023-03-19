#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author: 张福强
# datetime:2022/3/13 12:10 下午
# software: PyCharm

import os
import shutil
import subprocess

import pytest

from tools.Logger import log
from tools.allure_result import ModifyResult

if __name__ == "__main__":

    # 报告生成地址：
    result_path = './result/allure-results'
    if not os.path.exists(result_path):
        os.makedirs(result_path)

    """
        删除文件夹
    """
    if os.path.exists(result_path):
        shutil.rmtree(result_path)

    # 环境变量获取
    case = 'cases/test_demo.py'
    # case = 'cases/other/test_project_three_stage.py'
    # case = 'cases/other/test_project_three_stage.py::TestThreeStage::test_csv_classification_three_stage'
    # case = 'cases/act/test_init/'
    test_case = os.getenv("TEST_CASE")
    if not test_case:
        test_case = case

    # 修改ENV环境
    env = "test"
    test_env = os.getenv("TEST_ENV")
    if not test_env:
        test_env = env
    """
    生成报告
    """

    # os.system(f"pytest -vs {test_case} --env={test_env} --alluredir={result_path}")
    pytest.main(
        ['-v', '-s', '-q', test_case, '--env', test_env, '--alluredir', result_path])
    # 生成allure报告
    shell = f'allure generate {result_path}/ -o ./result/allure-report/ --clean'
    os.system(shell)
    # 发送钉钉推送结果
    send_report = os.getenv("SEND_REPORT")
    if send_report:
        mf = ModifyResult()
        mf.robot_send()




