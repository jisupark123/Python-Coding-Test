# 장난감 조립

"""
dp[x] 
-> 기본 부품(k)이 각각 몇개(v) 필요한지 (딕셔너리)
-> x가 기본 부품이라면 dp[x] = {x:1}
"""

import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):

    # a 만드는데 b부품 c개 필요
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

# dp[a] -> {b:c} = a 만드는데 b기본 부품 c개 필요
dp = [defaultdict(int) for _ in range(N + 1)]


def dfs(x):

    # 기본 부품이라면 dp[x] = {x:1}
    if len(graph[x]) == 0:
        dp[x][x] = 1
        return

    for b, c in graph[x]:

        if len(dp[b]) == 0:
            dfs(b)

        for k, v in dp[b].items():
            dp[x][k] += v * c


dfs(N)

for k, v in sorted(dp[N].items()):
    print(k, v)
