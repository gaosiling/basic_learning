#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
函数：
    python内置函数
    函数定义
    函数参数：
        位置参数(位置顺序)，默认参数(设置参数默认值，一般在最后)，可变参数（*args接收tuple），关键字参数(**kw接收dict)
"""


def a(i, j):
    return i ** j


def b():
    x = a(2, 8)
    print(x)


b()


# 默认参数
# def mr(a, b=2):
#     print(a + b)
#
#
# mr(1, 3)

# 可变参数
# def kb(a, b, *args):
#     c = a + b
#     for i in args:
#         c = c + i
#     print(c)
#
#
# t = (2, 3, 4, 1)
# kb(1, 1, *t)

# 关键字参数
# def gjz(a, b, *args, **kwargs):
#     c = 0
#     for i in args:
#         c = c + i
#     for k, v in kwargs.items():
#         d = k
#         e = v
#     print('name is:', a, 'age is:', str(b), 'score is:', str(c), d, 'is:', e)
#
#
# t = (11, 22)
# d = {'city': 'ty'}
# gjz('air', 12, *t, **d)

# 递归
def dj(a):
    if a == 1:
        return a
    else:
        return a * dj(a - 1)


print(dj(3))
# lambda匿名函数
