#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/23 13:17
# @Author  : ZHOU HAO
# @Site    : 
# @File    : 2020_E_3.py
# @Software: PyCharm

from queue import PriorityQueue

T = int(input())
for casenum in range(T):
    n = int(input())
    toy = []
    sum_time = 0
    for idx in range(n):
        [enjoy, remember] = [int(s) for s in input().split(" ")]
        toy.append([enjoy + remember, idx, enjoy, remember])
        sum_time += enjoy
    max_time = sum_time
    max_count = 0
    cur_time = sum_time
    count = n
    cur_toy = []
    toy_queue = PriorityQueue()
    for idx in range(n):
        [_, _, enjoy, remember] = toy[idx]
        if enjoy + remember <= sum_time:
            toy_queue.put((-enjoy - remember, idx, enjoy, remember))
            cur_time += enjoy
            if cur_time > max_time or (cur_time == max_time and count > max_count):
                max_time = cur_time
                max_count = count
        else:
            if cur_time > max_time or (cur_time == max_time and count > max_count):
                max_time = cur_time
                max_count = count
            toy_queue.put((-enjoy - remember, idx, enjoy, remember))
            cur_time += enjoy
            while not toy_queue.empty():
                (_, idx, enjoy, remember) = toy_queue.get()
                if enjoy + remember > sum_time:
                    cur_time -= enjoy * 2
                    sum_time -= enjoy
                    count -= 1
                else:
                    toy_queue.put((-enjoy - remember, idx, enjoy, remember))
                    break
    if toy_queue.empty():
        print("Case #{}: {} {}".format(casenum + 1, n - max_count, max_time))
    else:
        print("Case #{}: {} {}".format(casenum + 1, n - toy_queue.qsize(), 'INDEFINITELY'))








# T = int(input())
# for casenum in range(T):
#     n = int(input())
#     toy = []
#     for _ in range(n):
#         [enjoy, remember] = [int(s) for s in input().split(" ")]
#         # rate = remember / enjoy
#         toy.append((enjoy, remember))
#     hash_table = []
#     flag = 0
#     toy_copy = toy
#     while toy != []:
#         (cur_enjoy, cur_remember) = toy.pop(0)
#         if sum([each[0] for each in toy]) >= cur_remember:
#             toy.append((cur_enjoy, cur_remember))
#         if toy in hash_table:
#             flag = 1
#             break
#         else:
#             hash_table.append(toy)
#     if flag == 1:
#         print("Case #{}: {} {}".format(casenum + 1, n - len(toy), "INDEFINITELY"))
#     else:
#         toy = toy_copy
#         status = [0] * n
#         time = []
#         for i in range(n):
#             if i == 0:
#                 time.append([toy[i][0], 1])
#             else:
#                 time.append([time[-1][0] + toy[i][0], i + 1, 0])
#         for i in range(n):
#             maxtime = 0
#             maxnum = 0
#             for j in range(n + i - 1, i, -1):
#                 if time[j][0] > toy[i][1] and (time[j][2] == 1):
#                     time.append([time[j][0] + toy[i][0], time[j][1] + 1, 0])
#                     break
#                 elif time[j][2] == 0:
#                     if time[j][0] + toy[i][0] > maxtime:
#                         maxtime = time[j][0] + toy[i][0]
#                         maxnum = time[j][1] + 1
#                 time.append(maxtime, maxnum, 1)
#         time = time[n:]
#         maxindex = 0
#         maxtime = 0
#         maxnum = 0
#         for i in range(len(time)):
#             if time[i][0] > maxtime:
#                 maxtime = time[i][0]
#                 maxnum = time[i][1]
#         print("Case #{}: {} {}".format(casenum + 1, n - maxnum, maxtime))