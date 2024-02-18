# 최소비용 구하기 2

import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]  # graph[n] -> [(cost, node)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

start, end = map(int, input().split())

costs = [float("inf") for _ in range(n + 1)]

queue = [(0, start, [start])]  # (cost, node, [visited_nodes])

while queue:
    c, n, vn = heapq.heappop(queue)
    if n == end:
        print(c)
        print(len(vn))
        print(*vn)
        break

    for nc, nn in graph[n]:
        if costs[nn] > c + nc:
            costs[nn] = c + nc
            heapq.heappush(queue, (c + nc, nn, [*vn, nn]))
