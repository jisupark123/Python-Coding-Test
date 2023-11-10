# 모든 순열

N = int(input())

tmp = []


def dfs():
    if len(tmp) == N:
        print(*tmp)

    for i in range(1, N + 1):
        if i not in tmp:
            tmp.append(i)
            dfs()
            tmp.pop()


dfs()
