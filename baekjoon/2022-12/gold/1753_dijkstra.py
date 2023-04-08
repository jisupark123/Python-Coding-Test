# 최단경로
# 방향 있는 그래프의 다익스트라 알고리즘
from sys import stdin, maxsize
import heapq

max_size = maxsize
input = stdin.readline


def dijkstra():
    V, E = map(int, input().split())
    K = int(input())
    graph = [[] for _ in range(V + 1)]  # list[[가중치,노드],[가중치,노드]]
    costs = [max_size for _ in range(V + 1)]  # 모든 가중치를 무한대로 설정
    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a].append([c, b])

    costs[K] = 0
    queue = []  # list[거리,인덱스]
    queue.append([0, K])
    while queue:
        cost, node = heapq.heappop(queue)
        for next_cost, next_node in graph[node]:
            if costs[next_node] > cost + next_cost:
                costs[next_node] = cost + next_cost
                heapq.heappush(queue, [cost + next_cost, next_node])

    for cost in costs[1:]:
        if cost == maxsize:
            print("INF")
        else:
            print(cost)


dijkstra()
