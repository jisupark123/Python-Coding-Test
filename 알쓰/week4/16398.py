# 행성 연결

import sys
import heapq

input = sys.stdin.readline


N = int(input())
weight = [list(map(int, input().split())) for _ in range(N)]
visit = [False for _ in range(N)]
queue = [(weight[0][x], x) for x in range(1, N)]  # [(cost,node)]

res = 0

visit[0] = True
heapq.heapify(queue)

while queue:
    cost, node = heapq.heappop(queue)
    if visit[node]:
        continue
    visit[node] = True
    res += cost
    for i in range(N):
        if not visit[i] and weight[node][i] != 0 and i != node:
            next_cost = weight[node][i]
            next_node = i
            heapq.heappush(queue, (next_cost, next_node))

print(res)
