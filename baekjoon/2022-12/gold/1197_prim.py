# 최소 스패닝 트리(최소 신장 트리)
# 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리
# 프림 알고리즘을 사용
from sys import stdin
import heapq

input = stdin.readline


# 프림 알고리즘
# BFS와 유사하지만 선택지 중에 가장 최솟값을 가지는 간선을 택한다. (최소힙 사용)
def prim():
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]  # list[[노드,가중치]]
    visited = [False for _ in range(V + 1)]

    # 그래프 만들기
    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])  # a에서 b로 가는데 드는 가중치 c
        graph[b].append([a, c])

    res = 0
    queue = []
    queue.append([0, 1])

    while queue:
        curr_cost, curr_node = heapq.heappop(queue)
        if not visited[curr_node]:
            visited[curr_node] = True
            res += curr_cost
            for next_node, next_cost in graph[curr_node]:
                heapq.heappush(queue, (next_cost, next_node))

    return res


print(prim())
