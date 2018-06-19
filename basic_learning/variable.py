#!/usr/bin/env python3
# -*- coding:utf-8 -*-

name = '哥斯拉'
age = 18
gender = '男 '

# 格式化输出
print('name is ' + name + 'age is ' + str(age) + 'gender is ' + gender)
print('name is ', name, ';age is ', age, ';gender is ', gender)
print('name is %s, age is %d, gender is %s' % (name, age, gender))

print(int(12 / 3.3))

print("数据比例是 %.02f%%" % (0.1 * 100))
print("数据比例是 %f%%" % (0.1 * 100))

# 输入输出
# a = input('请输入：')
# print(a)

# python没有++
b = 1
b += 2
print(b)

# if elif else
c = 10
if c % 2 == 0:
    print('oushu')
elif c % 2 != 0:
    print('jishu')
else:
    print('not numbers')

# or、and 、not、is、is not、in、＞、＜、＝
