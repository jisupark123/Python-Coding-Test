# 최소비용 구하기

import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])

start, finish = map(int, input().split())

queue = []
heapq.heappush(queue, [0, start])
distance = [sys.maxsize for _ in range(N + 1)]
i = 0
while queue:
    cost, node = heapq.heappop(queue)
    if node == finish:
        print(cost)
        break
    for next_cost, next_node in graph[node]:
        if distance[next_node] > next_cost + cost:
            distance[next_node] = next_cost + cost
            heapq.heappush(queue, [cost + next_cost, next_node])
