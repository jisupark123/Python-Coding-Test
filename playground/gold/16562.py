# 친구비

import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())
costs = list(map(int, input().split()))
costs = sorted([(cost, i) for i, cost in enumerate(costs, 1)])

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

money = K
goal = N
visited = [0] * (N + 1)

for cost, i in costs:
    if visited[i]:
        continue

    if cost > money:
        print("Oh no")
        break

    money -= cost
    goal -= 1
    visited[i] = 1
    q = deque()
    q.append(i)
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if not visited[nx]:
                goal -= 1
                visited[nx] = 1
                q.append(nx)

    if goal == 0:  # 모든 노드가 친구
        print(K - money)
        break
