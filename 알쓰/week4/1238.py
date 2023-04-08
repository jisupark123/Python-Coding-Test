# 파티

import sys
import heapq

N, M, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])


def dijkstra(start, finish):
    distance = [sys.maxsize for _ in range(N + 1)]
    distance[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])

    while queue:
        cost, node = heapq.heappop(queue)
        if node == finish:
            return cost
        for next_cost, next_node in graph[node]:
            if distance[next_node] > cost + next_cost:
                distance[next_node] = cost + next_cost
                heapq.heappush(queue, [cost + next_cost, next_node])


res = []

for i in range(1, N + 1):
    res.append(dijkstra(i, X) + dijkstra(X, i))

print(max(res))
