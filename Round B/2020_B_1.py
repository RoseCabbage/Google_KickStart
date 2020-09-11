T = int(input())
for casenum in range(1, T + 1):
    N = int(input())
    height = [int(s) for s in input().split()]
    ans = 0
    for i in range(1, N - 1):
        if height[i] > height[i - 1] and height[i] > height[i + 1]:
            ans += 1
    print('Case #{}: {}'.format(casenum, ans))