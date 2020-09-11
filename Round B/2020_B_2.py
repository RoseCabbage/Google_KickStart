T = int(input())
for casenum in range(1, T + 1):
    N, D = [int(s) for s in input().split()]
    time = [int(s) for s in input().split()]
    time.reverse()
    for each in time:
        D = D // each * each
    print('Case #{}: {}'.format(casenum, D))