# 최소비용 구하기

import sys
import heapq

input = sys.stdin.readline
INF = float("INF")

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

start, end = map(int, input().split())


d = [INF for _ in range(N + 1)]
d[start] = 0
queue = [(0, start)]

while queue:
    cost, node = heapq.heappop(queue)
    if node == end:
        print(d[node])
        break
    for nc, nn in graph[node]:
        if d[nn] > cost + nc:
            d[nn] = cost + nc
            heapq.heappush(queue, (cost + nc, nn))
