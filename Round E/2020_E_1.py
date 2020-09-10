import numpy as np
T = int(input())
for casenum in range(T):
    length = int(input())
    nums = [int(s) for s in input().split(" ")]
    if length == 2:
        print("Case #{}: {}".format(casenum + 1, 2))
    else:
        diff = nums[2] - nums[1]
        curlen = 2
        maxlen = 2
        for i in range(2, length):
            if nums[i] - nums[i - 1] == diff:
                curlen += 1
            else:
                diff = nums[i] - nums[i - 1]
                maxlen = max(maxlen, curlen)
                curlen = 2
        maxlen = max(maxlen, curlen)
        print("Case #{}: {}".format(casenum + 1, maxlen))

