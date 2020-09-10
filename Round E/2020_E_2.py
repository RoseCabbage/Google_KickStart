#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/23 12:10
# @Author  : ZHOU HAO
# @Site    :
# @File    : 2020_E_2.py
# @Software: PyCharm

T = int(input())
for casenum in range(T):
    [n, left, right, public] = [int(s) for s in input().split(" ")]
    if n == 1:
        if left != 1 or right != 1 or public != 1:
            print("Case #{}: {}".format(casenum + 1, "IMPOSSIBLE"))
        else:
            print("Case #{}: {}".format(casenum + 1, 1))
    elif left + right - public > n:
        print("Case #{}: {}".format(casenum + 1, "IMPOSSIBLE"))
    else:
        other = n - (left + right - public)
        res = []
        if left != public:
            res += [n - 1] * (left - public)
            res += [n - 2] * other
            res += [n] * public
            res += [n - 1] * (right - public)
            if min(res) < 1:
                print("Case #{}: {}".format(casenum + 1, "IMPOSSIBLE"))
            else:
                print("Case #{}: {}".format(casenum + 1, " ".join([str(num) for num in res])))
        elif right != public:
            res += [n - 1] * (left - public)
            res += [n] * public
            res += [n - 2] * other
            res += [n - 1] * (right - public)
            if min(res) < 1:
                print("Case #{}: {}".format(casenum + 1, "IMPOSSIBLE"))
            else:
                print("Case #{}: {}".format(casenum + 1, " ".join([str(num) for num in res])))
        else:
            if public == 1 and n > 1:
                print("Case #{}: {}".format(casenum + 1, "IMPOSSIBLE"))
            else:
                res = [n]
                res += [n - 1] * other
                res += [n] * (public - 1)
                if min(res) < 1:
                    print("Case #{}: {}".format(casenum + 1, "IMPOSSIBLE"))
                else:
                    print("Case #{}: {}".format(casenum + 1, " ".join([str(num) for num in res])))