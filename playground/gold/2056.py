# 작업

import sys

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N + 1)]
dp = [0] * (N + 1)

for i in range(1, N + 1):
    tmp = list(map(int, input().split()))
    dp[i] = tmp[0]
    graph[i] = tmp[2 : 2 + tmp[1]]

for i in range(1, N + 1):
    time = 0
    for x in graph[i]:
        time = max(time, dp[x])
    dp[i] += time

print(max(dp))
