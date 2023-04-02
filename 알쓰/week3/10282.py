# 해킹

import sys
import heapq

input = sys.stdin.readline


for _ in range(int(input())):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(10001)]  # graph[n] -> 노드 n이 가리키는 그래프의 [cost,node]
    for _ in range(d):
        a, b, s = map(int, input().split())  # b가 a를 가리킴 (가중치 s)
        graph[b].append([s, a])
    total_node = set([c])
    total_cost = 0
    queue = graph[c]
    heapq.heapify(queue)
    while queue:
        cost, node = heapq.heappop(queue)
        if not node in total_node:
            total_node.add(node)
            total_cost = max(total_cost, cost)
            for next_cost, next_node in graph[node]:
                heapq.heappush(queue, [cost + next_cost, next_node])

    print(len(total_node), total_cost)
