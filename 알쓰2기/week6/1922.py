# 네트워크 연결

import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

INF = float("inf")

graph = [[] * N for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a - 1].append((c, b - 1))
    graph[b - 1].append((c, a - 1))


visited = [0] * N
ans = 0
queue = [(0, 0)]

while queue:
    cost, node = heapq.heappop(queue)
    if not visited[node]:
        visited[node] = 1
        ans += cost
        for nc, nn in graph[node]:
            heapq.heappush(queue, (nc, nn))

print(ans)
