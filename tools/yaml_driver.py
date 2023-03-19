# -*- coding: utf-8 -*-
# @Time    : 2021/3/16 7:30 下午
# @Author  : 张福强
# @Email   : mat_wu@163.com
# @File    : yaml_driver.py
# @Software: PyCharm
import yaml

from const import ROOT_PATH


class YamlDriver(object):
    def __init__(self, path):
        self.config_path = path
        with open(self.config_path, encoding="utf-8") as f:
            self.all_data = list(yaml.safe_load_all(f))
            self.data = self.all_data[0]

    def set_data(self, data):
        # logger.info(f"写入数据：{data}")
        with open(self.config_path, 'w+', encoding='utf-8') as f:
            yaml.safe_dump(data, f, allow_unicode=True, sort_keys=False)

    def set_value(self, key, value):
        # logger.info(f"写入数据-key:{key}, value:{value}")
        if self.data is None:
            self.data = {}
        self.data[key] = value
        self.set_data(self.data)

    def get_all_data(self):
        return self.data

    def get_base_config(self, name):
        value = self.data['base_config'][name]
        return value

    def get_base_info(self, name):
        value = self.data['base_info'][name]
        return value

    def get_user_info(self, name):
        value = self.data['user_info'][name]
        return value

    def get_db_info(self, name):
        info: dict = self.data['db_info'][name]
        info_list = info.values()
        return info_list

    def get_init_params(self, name):
        value = self.data['init_params'][name]
        return value

    def get_modal_task_data(self, name):
        value = self.data['modal_task_data'][name]
        return value

    def get_value(self, key):
        return self.data[key]


if __name__ == '__main__':
    # ry = ReadYaml("D:\\code\\python_workplace\\act_api_auto\\config\\prod\\config.yaml")
    # resp = ry.get_init_params("project_id")
    resp = YamlDriver(ROOT_PATH+'/config/test/config.yaml').get_base_info('url')
    print(resp)