#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/30 13:56
# @Author  : ZHOU HAO
# @Site    : 
# @File    : 2020_C_1.py
# @Software: PyCharm

T = int(input())
for casenum in range(T):
    [N, K] = [int(s) for s in input().split(" ")]
    nums = [int(s) for s in input().split(" ")]
    flag = 0
    count = 0
    for idx, num in enumerate(nums):
        if num == K:
            flag = 1
        else:
            if flag == 1 and nums[idx - 1] - num != 1:
                flag = 0
        if flag == 1 and num == 1:
            count += 1
    print('Case #{}: {}'.format(casenum + 1, count))