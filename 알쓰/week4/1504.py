# 특정한 최단 경로

# 방법이 두가지 존재
# 1. 시작점 -> v1 -> v2 -> N
# 2. 시작점 -> v2 -> v1 -> N

# 시작점, v1, v2에 대한 거리 테이블을 모두 구해준 다음
#
# (시작점 -> v1) + (v1 -> v2) + (v2 -> N)
# (시작점 -> v2) + (v2 -> v1) + (v1 -> N)
# 둘 중 최솟값을 출력한다

import sys
import heapq

input = sys.stdin.readline
N, E = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])

v1, v2 = map(int, input().split())


def dijkstra(start):
    queue = []
    distance = [sys.maxsize for _ in range(N + 1)]
    distance[start] = 0
    heapq.heappush(queue, [0, start])

    while queue:
        cost, node = heapq.heappop(queue)
        for c, n in graph[node]:
            next_cost = cost + c
            if distance[n] > next_cost:
                distance[n] = next_cost
                heapq.heappush(queue, [next_cost, n])
    return distance


_start = dijkstra(1)
_v1 = dijkstra(v1)
_v2 = dijkstra(v2)

res = min(_start[v1] + _v1[v2] + _v2[N], _start[v2] + _v2[v1] + _v1[N])
print(res if res < sys.maxsize else -1)
