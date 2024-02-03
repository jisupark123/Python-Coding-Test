# 도시 분할 계획

"""
1. 프림 알고리즘으로 최소 신장 트리 생성
2. 가장 큰 가중치 제거
"""

import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())

# graph[n] -> [(cost, node)] -> 노드로 이동하는데 드는 비용
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

visited = [0] * (N + 1)

queue = [(0, 1)]
max_cost = 0  # 가중치 중 최댓값
sum_cost = 0  # 가중치의 합

while queue:
    cost, node = heapq.heappop(queue)

    if not visited[node]:
        visited[node] = 1
        max_cost = max(max_cost, cost)
        sum_cost += cost

        for next_cost, next_node in graph[node]:
            if not visited[next_node]:
                heapq.heappush(queue, (next_cost, next_node))

print(sum_cost - max_cost)
