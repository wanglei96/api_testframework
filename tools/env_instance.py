#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/25 10:48
# @Author  : 王磊
# @File    : env_instance.py
# @Software: PyCharm
import os

from const import ROOT_PATH
from tools.yaml_driver import YamlDriver


class EnvInstance:

    def __init__(self, env_name):
        self.env_name = env_name
        self.config_path = os.path.join(ROOT_PATH,
                                   "config",
                                   self.env_name,
                                   "config.yaml")

    def create(self):
        return YamlDriver(self.config_path)


if __name__ == "__main__":
    print(EnvInstance('test').create())