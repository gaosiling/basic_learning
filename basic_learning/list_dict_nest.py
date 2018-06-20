#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# list和dict嵌套
listL = [{'a': 1, 'b': 2}, {'c': 3}, {'d': 4, 'e': 5, 'f': 6}]
for i in listL:
    for k, v in i.items():
        print(k, '=', v, end='\t')
    print(end='\n')

# list删除
listD = [1, 2, 3, 4, 5]
print(2 not in listD)

for i in range(1, listD.__len__() + 1):
    print(listD.__len__())
    listD.remove(i)  # 删除i这个元素，pop()删除对应下标
print(listD)

for i in range(0, listD.__len__()):
    listD.pop(0)  # 每次都删除第一个，删除i次
    print(listD)
for i in range(listD.__len__()-1, -1, -1):
    listD.pop(i)    # 从最后一位开始向前删除
    print(listD)

