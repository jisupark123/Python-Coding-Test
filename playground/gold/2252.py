# 줄 세우기

import sys

input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

ans = []
q = deque()

for x in range(1, N + 1):
    if indegree[x] == 0:
        q.append(x)

while q:
    x = q.popleft()
    ans.append(x)
    for nx in graph[x]:
        indegree[nx] -= 1
        if indegree[nx] == 0:
            q.append(nx)

print(*ans)
