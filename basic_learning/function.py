#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
有无参
有无返回值
位置参数，默认参数，可变参数（*args），关键字参数
"""


def a(i, j):
    return i ** j


def b():
    x = a(2, 8)
    print(x)


b()
