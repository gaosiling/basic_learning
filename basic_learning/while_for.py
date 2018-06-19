#!/usr/bin/env python3
# -*- coding:utf-8 -*-

a = 1
s = 0
while a <= 2:
    s += a
    a += 1
print(s, '\n')

b = 0
while b <= 10:
    if b % 2 == 0:
        print(b)
    b += 1

for i in range(1, 11, 2):
    print(i)
for i in range(1, 10):
    for j in range(1, i + 1):
        print('%s*%s=%s' % (i, j, i * j), end='\t')
    print('')
