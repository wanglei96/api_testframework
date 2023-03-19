# -*- coding: utf-8 -*-
# @File   : db_connect
# @Time   : 2022/7/1 14:21 
# @Author : 张福强
import pymysql
from pyhive import hive
import pyhdfs
import phoenixdb
import phoenixdb.cursor

from const import CONFIG_PATH, ROOT_PATH
from tools.Logger import log
from tools.yaml_driver import YamlDriver


class DbConnect(object):
    """
    封装Mysql/Oracle/Hive数据库基本操作函数
    """

    def __init__(self, connect_type, env: YamlDriver = None):
        """
        :param env:
        :param connect_type: mysql / oracle / hive / HDFS / Hbase / clickhouse
        """

        self.global_config = YamlDriver(CONFIG_PATH + 'config.yaml')
        if env is None:
            self.env = self.global_config.get_value('env')
            self.config = YamlDriver(ROOT_PATH + f'/config/{self.env}/config.yaml')
        self._host, self._port, self._user, self._password, self._database = env.get_db_info(connect_type)
        self._logger = log
        self._connect_type = connect_type
        self.conn = None
        self.cursor = None

    def connect_db(self):
        """
        建立数据库连接
        :return: 是否连接成功
        """
        try:
            if self._connect_type == 'mysql':
                # print("self._host",self._host,"self._port",self._port,"self._user",self._user,"self._password",self._password,"self._database",self._database)
                self.conn = pymysql.connect(host=self._host, password=self._password, user=self._user, port=self._port,
                                            database=self._database,  charset='utf8', connect_timeout=10)
                self.cursor = self.conn.cursor()  # 使用cursor()方法获取操作游标
            elif self._connect_type == 'hive':
                self.conn = hive.Connection(host=self._host, port=self._port, database=self._database, auth="NONE", username=self._user, password=self._password)
                self.cursor = self.conn.cursor()
            elif self._connect_type == 'HDFS':
                self.conn = pyhdfs.HdfsClient(hosts=self._host, user_name=self._user)
            elif self._connect_type == 'hbase':
                self.conn = phoenixdb.connect(url=f"http://{self._host}:{self._port}", autocommit=True)
                self.cursor = self.conn.cursor()
        except Exception as e:
            self._logger.error("connectDatabase failed")
            print(e)
            return False
        return True

    def close(self):
        """
        关闭游标和数据库连接
        :return:
        """
        if self.conn and self.cursor:
            self.cursor.close()
            self.conn.close()
        else:
            pass
        return True

    def execute(self, sql, params=None, commit=False):
        """
        执行数据库的sql语句
        :param sql:
        :param params:
        :param commit:
        :return:
        """
        res = self.connect_db()  # 连接数据库
        row_count = None
        if not res:
            return False
        try:
            if self.conn and self.cursor:
                row_count = self.cursor.execute(sql, params)  # execute循环单条插入
                # print("execute成功")
                # rowcount = self.cursor.executemany(sql, params) # executemany批量插入
                # print(rowcount)
                if commit:
                    self.conn.commit()
                else:
                    pass
        except Exception as e:
            self._logger.error("execute failed: " + sql)
            self._logger.error("params: " + str(params))
            print(e)
            # self.conn.rollback()  # 发生错误时会滚
            self.close()
            return False
        return row_count

    def fetchall(self, sql, params=None):
        """
        fetchall() 方法获取所有数据
        :param sql:
        :param params:
        :return:
        """
        res = self.execute(sql, params)
        # if not res:
        #     self._logger.info("查询失败")
        #     return False
        # self.close()
        results = self.cursor.fetchall()
        self._logger.info("查询成功" + str(results))
        return results

    def fetchone(self, sql, params=None):
        """
        fetchone() 方法获取一条数据
        :param sql:
        :param params:
        :return:
        """
        res = self.execute(sql, params)
        if not res:
            self._logger.info("查询失败")
            return False
        self.close()
        result = self.cursor.fetchone()
        self._logger.info("查询成功" + str(result))
        return result

    def edit(self, sql, params=None):
        """
        增删改数据库操作
        :param params:
        :param sql:
        :return:
        """
        res = self.execute(sql, params, True)
        if not res:
            self._logger.info("操作失败")
            return False
        self.conn.commit()
        self.close()
        self._logger.info("操作成功" + str(res))
        return res


if __name__ == '__main__':
    pass
    # mysql连接
    # mysql_conn = DbConnect("10.0.0.0", "bigdata", "bigdata", 66666, "database")
    # sql = "select * from database.table limit %s;"
    # values = 1
    # result1 = mysql_conn.fetchall(sql, 'Mysql', values)
    # result2 = mysql_conn.fetchone(sql, 'Mysql', values)
    #
    # # hive连接
    # hive_conn = DbConnect("10.0.0.0", None, None, 10000, "database")
    # sql = "select * from database.table limit1;"
    # result = hive_conn.fetchall(sql, 'Hive')
    #
    # # clickhouse连接
    # cconn = DbConnect("10.0.0.0", "bigdata", "bigdata", 66666, "database")
    # sql = "select * from database.table limit 1;"
    # result = cconn.click_house_execute(sql)
    # print(result)
