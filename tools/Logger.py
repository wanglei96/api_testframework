# Author: 张福强
# *_*coding:utf-8 *_*
import logging
import time
import os
from loguru import logger

import const


class Logings:

    class PropogateHandler(logging.Handler):
        def emit(self, record) -> None:
            logging.getLogger(record.name).handle(record)

    __instance = None

    rq = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))

    logger.add(PropogateHandler(), format="{time:YYYY-MM-DD HH:mm:ss}  | {level}> {elapsed}  | {message}")

    log_path = const.LOG_PATH
    # 判断目录是否存在，不存在则创建新的目录
    if not os.path.isdir(log_path): os.makedirs(log_path)
    logger.add('{}{}.log'.format(log_path, rq),  # 指定文件
               format="{time:YYYY-MM-DD HH:mm:ss}  | {level}> {elapsed}  | {message}",
               encoding='utf-8',
               retention='1 days',  # 设置历史保留时长
               backtrace=True,  # 回溯
               diagnose=True,  # 诊断
               enqueue=True,  # 异步写入
               # rotation="5kb",  # 切割，设置文件大小，rotation="12:00"，rotation="1 week"
               # filter="my_module"  # 过滤模块
               # compression="zip"   # 文件压缩
               )

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Logings, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    def info(self, msg, *args, **kwargs):
        return logger.info(msg, *args, **kwargs)

    def debug(self, msg, *args, **kwargs):
        return logger.debug(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        return logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        return logger.error(msg, *args, **kwargs)

    def exception(self, msg, *args, exc_info=True, **kwargs):
        return logger.exception(msg, *args, exc_info=True, **kwargs)


log = Logings()

if __name__ == '__main__':
    log.info("11111")
