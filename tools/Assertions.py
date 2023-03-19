#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/11/28 15:38
# @Author  : 王磊
# @File    : Assertions.py
# @Software: PyCharm
import jmespath

from tools.Logger import log


class Assertions:

    @staticmethod
    def equal(a, b, text):
        """
        断言相等
        :param a: 预期值
        :param b: 实际值
        :param text: 错误描述
        :return:
        """
        log.info(f'预期:【{a}】等于:【{b}】')
        assert a == b, text

    @staticmethod
    def value_in(a, b, text):
        """
        断言包含
        :param a: 预期值
        :param b: 实际值
        :param text: 错误描述
        :return:
        """
        log.info(f'预期:【{a}】在:【{b}】中')
        assert a in b, text

    @staticmethod
    def not_equal(a, b, text):
        """
        断言不等
        :param a: 预期值
        :param b: 实际值
        :param text: 错误描述
        :return:
        """
        log.info(f'预期:【{a}】不等于:【{b}】')
        assert a != b, text

    @staticmethod
    def equals(a, b, text):
        """
        断言多值相等
        :param a: 预期值
        :param b: 实际值，可迭代对象
        :param text: 错误描述
        :return:
        """
        log.info(f'预期:【{b}】都等于:【{a}】')
        for i in b:
            if i != a:
                assert False, text

    @staticmethod
    def value_not_in(a, b, text):
        """
        断言不包含
        :param a: 预期值
        :param b: 实际值
        :param text: 错误描述
        :return:
        """
        log.info(f'预期:【{a}】不在:【{b}】中')
        assert a not in b, text

    @staticmethod
    def values_in(a: list, b, text):
        """
        断言列表值都在对象b中
        :param a: 预期值
        :param b: 实际值
        :param text: 错误描述
        :return:
        """
        log.info(f'预期:【{a}】都在:【{b}】中')
        for i in a:
            if i not in b:
                assert False, text
