import numpy as np

T = int(input())
for casenum in range(T):
    K = int(input())
    note = [int(s) for s in input().split(" ")]
    pre = [0, 0, 0, 0]
    for i in range(1, K):
        new = []
        if note[i] == note[i - 1]:
            for idx_new in range(4):
                minnum = np.inf
                for idx_old in range(4):
                    if idx_new == idx_old:
                        minnum = min(minnum, pre[idx_old])
                    else:
                        minnum = min(minnum, pre[idx_old] + 1)
                new.append(minnum)
        elif note[i] > note[i - 1]:
            for idx_new in range(4):
                minnum = np.inf
                for idx_old in range(4):
                    if idx_new > idx_old:
                        minnum = min(minnum, pre[idx_old])
                    else:
                        minnum = min(minnum, pre[idx_old] + 1)
                new.append(minnum)
        else:
            for idx_new in range(4):
                minnum = np.inf
                for idx_old in range(4):
                    if idx_new < idx_old:
                        minnum = min(minnum, pre[idx_old])
                    else:
                        minnum = min(minnum, pre[idx_old] + 1)
                new.append(minnum)
        pre, new = new, []
    print("Case #{}: {}".format(casenum + 1, min(pre)))
