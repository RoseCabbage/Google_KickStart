T = int(input())
for i in range(T):
    N = int(input())
    num = [int(s) for s in input().split(" ")]
    if N == 1:
        print("Case #{}: {}".format(i+1, 1))
    else:
        count = 0
        maxnum = num[0]
        for cur in range(N - 1):
            if cur == 0 and num[cur] > num[cur + 1]:
                count += 1
            if num[cur] > maxnum and num[cur] > num[cur + 1]:
                count += 1
                maxnum = num[cur]
        if num[-1] > maxnum:
            count += 1
        print("Case #{}: {}".format(i+1, count))
