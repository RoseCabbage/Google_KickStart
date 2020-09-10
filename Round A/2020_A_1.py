#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 19:52
# @Author  : ZHOU HAO
# @Site    : 
# @File    : 2020_A_1.py
# @Software: PyCharm

T = int(input())
for casenum in range(T):
    [N, budget] = [int(s) for s in input().split()]
    price = [int(s) for s in input().split()]
    price.sort()
    cur_sum = 0
    ans = 0
    for idx in range(N):
        if budget >= price[idx]:
            ans += 1
            budget -= price[idx]
    print('Case #{}: {}'.format(casenum + 1, ans))