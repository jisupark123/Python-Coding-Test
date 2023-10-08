# 차량 배치

import sys
from collections import deque


input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

INF = 1e9

costs = [INF for _ in range(N + 1)]
costs[1] = 0
queue = deque()
queue.append((0, 1))  # cost, idx

while queue:
    cost, node = queue.popleft()
    for next_node in graph[node]:
        if costs[next_node] > cost + 1:
            costs[next_node] = cost + 1
            queue.append((cost + 1, next_node))

res = 0


# def dfs(idx_lst):
#     global res
#     res += 1
#     if idx_lst[-1] == len(costs):
#         return
#     s = set(list(map(lambda x: costs[x], idx_lst)))
#     for i in range(idx_lst[-1] + 1, len(costs)):
#         if costs[i] not in s:
#             idx_lst.append(i)
#             dfs(idx_lst)


# for i in range(1, len(costs)):
#     dfs([i])


print(res % (1e9 + 7))
