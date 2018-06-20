#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# cards = {'name': 'a', 'age': 11}
# for i, j in cards.items():
#     print(i, '==', j)
# cards['name'] = 'A'
# print(cards)

stu = {
    1: {
        'name': 'a',
        'age': 11
    },
    2: {
        'name': 'b',
        'age': 22
    },
    3: {
        'name': 'c',
        'age': 33
    }
}
# print(stu.__len__())
# stu.pop(3)    # 删除k对应的v
# print(stu)
# stu[1]['name'] = 'd'  # 修改
# print(stu)

# stu[4] = {'name': 'f', 'age': 44} # 添加k-v
# print(stu)

# print(stu.get(3).get('name'))

# print(stu.values())  # 返回所有值
# s = stu.copy()  # 复制一个字典
# print(s)

print(3 in stu)  # 判断k是否在字典中
# stu.clear()  # 清空
# print(stu)
# del stu  # 删除后无法访问

for i in stu.values():
    for j in i.values():
        print(j, end='\t')
    print(end='\n')

for a, b in stu.items():
    for x, y in b.items():
        print(a, '::', x, ' is ', y)
