# -*- coding: utf-8 -*-
# @Time    : 2022/5/20 15:43 上午
# @Author  : 张福强
# @File    : allure_result.py
import os
import json
from dingtalkchatbot.chatbot import DingtalkChatbot

import const


class ModifyResult(object):
    def __init__(self):

        self.pass_num = 0
        self.fail_num = 0

        results_path = const.RESULTS
        path_list = os.listdir(results_path)  # 列出文件夹下所有的目录与文件
        self.paths = []  # 找到需要修改的文件
        self.image_paths = []
        for i in range(0, len(path_list)):
            # 获取每个文件的路径
            path = os.path.join(results_path, path_list[i])
            # 只获取json文件
            if 'result.json' in path:
                self.paths.append(path)
            # 图片路径存储
            if 'attachment.png' in path:
                self.image_paths.append(path)

    def get_result(self):
        for index, path in enumerate(self.paths):
            with open(path, 'r', encoding='utf-8') as f:
                content = json.loads(f.read())
                if 'pass' in content['status']:
                    self.pass_num += 1
                elif 'fail' in content['status']:
                    self.fail_num += 1

    def robot_send(self, webhook=None, secret=None):
        """
        # 向钉钉发送报告。
        :param webhook:
        :param secret:
        :return:
        """

        # 数据统计
        self.get_result()
        flag = "成功" if self.fail_num == 0 else "失败"

        if not webhook:
            webhook = "https://oapi.dingtalk.com/robot/send?access_token=2028e715b6bfa0bb80cf1b1ade7f9a341defc28655b2f98b2710e392e8d7cbb8"
        if not secret:
            secret = "SECe71a6c5daa4dfc92de02bdbdee5c22836eb98f5e02f1e5f6390e5e390055e3b7"

        ding_talk = DingtalkChatbot(webhook=webhook, secret=secret)
        at_mobiles = ['17724272486']
        msg = "执行状态：{}，详细请点击查看!".format(flag)
        ding_talk.send_link(title='act API自动化测试报告', text=msg,
                            message_url="http://192.168.50.24:15252/allure-docker-service-ui/projects/auto-auto-api",
                            pic_url="https://avatars.githubusercontent.com/u/5879127?s=200&v=4")
