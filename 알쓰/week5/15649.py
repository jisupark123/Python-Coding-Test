# N과 M (1)

N, M = map(int, input().split())


def dfs(s):
    if len(s) == M:
        print(" ".join(s))
        return
    for i in range(1, N + 1):
        if str(i) not in s:
            dfs(s + str(i))


dfs("")
