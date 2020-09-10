def dfs(start, depth):
    path[depth] = start
    if depth >= A:
        fa[start] = path[depth - A]
    if depth >= B:
        fb[start] = path[depth - B]
    for one_node in node[start]:
        dfs(one_node, depth + 1)


T = int(input())
for casenum in range(T):
    N, A, B = [int(s) for s in input().split(" ")]
    tree = [int(s) for s in input().split(" ")]
    fa, fb, path = [-1] * N, [-1] * N, [-1] * N
    node = [[] for _ in range(N + 1)]
    for i, idx in enumerate(tree):
        node[idx - 1].append(i + 1)
    dfs(0, 0)
