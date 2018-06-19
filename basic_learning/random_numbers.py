#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import random

# randomint闭区间，randomrange开区间
for i in range(1, 10):
    a = random.randint(1, 5)
    print(a)

# 猜拳（0：石头，1：剪刀，2：布）
computer = random.randint(0, 2)
try:
    player = int(input('请输入0-2其中一个数字（0：石头，1：剪刀，2：布）：'))
    if 0 <= player <= 2:
        if player == 0 and computer == 1 or player == 1 and computer == 2 or player == 2 and computer == 0:
            print('你赢了！')
        elif player == computer:
            print('平局')
        else:
            print('你输了。。。')
    else:
        print('请输入正确数字！')
except ValueError as e:
    print('请输入正确数字')
finally:
    pass
