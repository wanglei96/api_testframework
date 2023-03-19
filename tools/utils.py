import copy
import hashlib
import json
import platform
import ssl
import time
import datetime

import websocket

import const


def get_file_md5(file_path):
    """"
        获取文件的md5
    """
    with open(file_path, 'rb') as fp:
        data = fp.read()
    md5 = hashlib.md5(data).hexdigest()
    return md5


"""
    获取chromedriver路径
"""


def get_chromedriver():
    host_os = platform.system()
    print("操作系统:{}".format(host_os))
    chromedriver_path = const.CHROMEDRIVER
    path = None
    if host_os == 'Windows':
        path = chromedriver_path + "chromedriver.exe"
    elif host_os == 'Linux':
        path = chromedriver_path + "chromedriver"
    print("linux_chromedriver路径:{}".format(path))
    return path


def get_timestamp():
    """
        获取当前时间戳
    """
    t = time.time()
    now_time = int(round(t * 1000))
    return now_time


def sleep_time(logger, times):
    logger.info("强制等待{}秒".format(times))
    time.sleep(times)


def get_date_timestamp(date_str="", days=None, format_type="%Y%m%d"):
    """
    获取该日期的时间戳
    :param format_type: 今天：%Y%m%d, 时间戳："%Y-%m-%d %H:%M:%S"
    :param days: 加减天数
    :param date_str: 日期字符串
    :return: 返回该日期的时间戳
    """

    if date_str != "":
        time_array = time.strptime(date_str, format_type)
        timestamp = int(time.mktime(time_array))
    else:
        now = datetime.datetime.now()
        if days is None:
            timestamp = now.strftime(format_type)
        else:
            yes = now + datetime.timedelta(days=days)
            timestamp = yes.strftime(format_type)

    return timestamp


def date_str_change_timestamp(date_str, format_type='%Y-%m-%d %H:%M:%S'):
    return time.mktime(time.strptime(date_str, format_type))


"""
    获取配置文件的modal_task_data
"""


def get_modal_task_data(env, task_keyword):
    """
    :param env:
    :param task_keyword: 关键字详见配置文件 modal_task_data
    :return: 返回modal_type, task_type
    """
    modal_task_data: str = env.get_modal_task_data(task_keyword)
    modal_type, task_type = modal_task_data.split(",")
    return int(modal_type), int(task_type)


class Ws:

    def __init__(self, env, user_id):
        self.url = env.get_base_info('socket_url')
        self.user_id = user_id
        self.ws = None

    def connect(self):
        self.ws = websocket.create_connection(self.url, sslopt={"cert_reqs": ssl.CERT_NONE}, timeout=3600)
        self.ws.send('{{"event":"set_socket_info","data":{{"user_id": {}}}}}'.format(self.user_id))

    def rev_msg(self):
        msg = json.loads(self.ws.recv())

        return msg

    def send_msg(self, content):
        self.ws.send(json.dumps(content))

    def close(self):
        self.ws.close()

if __name__ == '__main__':
    print(get_date_timestamp(days=4))