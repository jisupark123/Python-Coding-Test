# 트리의 부모 찾기

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(1, N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


res = [-1 for _ in range(N + 1)]


def dfs(n):
    for node in graph[n]:
        if res[node] == -1:
            res[node] = n
            dfs(node)


dfs(1)
for n in res[2:]:
    print(n)
