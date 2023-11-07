# 중량제한

import sys
import heapq

input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]  # list[[가중치,노드],[가중치,노드]]
for _ in range(N):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

target_a, target_b = map(int, input().split())

weights = [0 for _ in range(N + 1)]

weights[target_a] = 0
queue = [(0, target_a)]

while queue:
    cost, node = heapq.heappop(queue)
    cost = -cost
    for nc, nn in graph[node]:
        if max(cost, nc) > weights[nn]:
            weights[nn] = max(cost, nc)
            heapq.heappush(queue, (-max(cost, nc), nn))

print(weights[target_b])
