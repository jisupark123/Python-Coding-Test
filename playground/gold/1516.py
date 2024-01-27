# 게임 개발

import sys

input = sys.stdin.readline


def dfs(x):
    for nx in graph[x]:
        if not visited[nx]:
            visited[nx] = 1
            dfs(nx)
            rank.append(nx)


N = int(input())
graph = [[] for _ in range(N + 1)]
values = [0] * (N + 1)

for a in range(1, N + 1):
    tmp = list(map(int, input().split()))[:-1]
    values[a] = tmp[0]
    for b in tmp[1:]:
        graph[a].append(b)


rank = []
visited = [0] * (N + 1)

for x in range(1, N + 1):
    if not visited[x]:
        visited[x] = 1
        dfs(x)
    rank.append(x)

dp = [0] * (N + 1)

for x in rank:
    max_time = 0
    for n in graph[x]:
        max_time = max(max_time, dp[n])

    dp[x] = max_time + values[x]

for num in dp[1:]:
    print(num)
