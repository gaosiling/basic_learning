#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# list列表 有序可变
listA = [1, 3, 2, 4]
# print(listA)

# 在末尾追加
# listA.append('a')
# print(listA)

# 指定位置添加
# listA.insert(0, 123)
# print(listA)

# 将B添加到A
# listB = [33, 55, 77, 99]
# listA.extend(listB)
# print(listB)
# print(listA)

# 遍历
# for i in listA:
#     print(i, end='\t')

# 取出对应索引的值
# print(listA[2])
# 列表中元素的个数
# print(listA.count(2))
# 找到元素的下标
# print(listA.index(3))

# 删除对应下标的元素
# print(listA.pop(3))  # 有返回值
# print(listA)
# print(listA.remove(2))  # 无返回值
# print(listA)
# del listA[1]
# print(listA)

# 反转排序，排序针对同类型
# print(listA)
# listA.reverse()
# print(listA)
# listA.sort()  # 默认升序
# print(listA)
# listA.sort(reverse=True)  # 降序
# print(listA)

# 长度最大最小
print(listA.__len__())
print(len(listA))
print(max(listA))
print(min(listA))

# del listA  # 删除后无法访问,会报错
# print(listA)
# listA.clear()
# print(listA)

# 切片不顾尾
print(listA[1:])
print(listA[:2])
print(listA[1:2])
print(listA[:])
print(listA[1::2])  # 步长间隔多少个元素取值

listC = list(x + y for x in range(1, 5) for y in range(11, 15) if x % 2 == 0 if y % 2 != 0)
print(listC)
listD = list(i + j for i in 'abc' for j in '123')
print(listD)
