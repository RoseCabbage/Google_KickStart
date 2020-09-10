#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 22:08
# @Author  : ZHOU HAO
# @Site    : 
# @File    : 2020_A_2.py
# @Software: PyCharm
T = int(input())
for casenum in range(T):
    N, K, B = [int(s) for s in input().split()]
    value = []
    for _ in range(N):
        value.append([int(s) for s in input().split()])
    for i in range(N):
        for j in range(1, K):
            value[i][j] += value[i][j - 1]
        value[i].append(0)
    dp = [[0] * (B + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, B + 1):
            for idx in range(min(K, j) + 1):
                dp[i][j] = max(dp[i][j], dp[i - 1][j - idx] + value[i - 1][idx - 1])
                # print(i, j, dp[i][j])
    print('Case #{}: {}'.format(casenum + 1, dp[N][B]))

