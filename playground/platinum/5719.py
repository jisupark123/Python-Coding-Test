# 거의 최단 경로

"""
1. 다익스트라 사용해서 출발지부터 다른 모든 노드까지 최단 거리 구하기
2. 도착지부터 역추적해서 최단거리 경로 삭제
- 처음에 그래프 생성할 때 반대로 이동하는 방향 그래프도 같이 생성
- 도착지부터 bfs 돌면서 경로 삭제
3. 최단거리 경로가 삭제된 그래프로 다시 최단거리 구하기 (다익스트라 사용)
"""

import sys
import heapq
from collections import deque

input = sys.stdin.readline

while True:
    N, M = map(int, input().split())
    if (N, M) == (0, 0):
        exit(0)

    start, end = map(int, input().split())

    graph = [set() for _ in range(N)]  # (cost, v)
    backprop = [set() for _ in range(N)]  # 출발 노드와 도착 노드를 바꾼 그래프

    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].add((c, b))
        backprop[b].add((c, a))

    # 첫번째 다익스트라
    q = [(0, start)]
    costs = [float("inf")] * N
    costs[start] = 0

    while q:
        c, v = heapq.heappop(q)
        for nc, nv in graph[v]:
            if c + nc < costs[nv]:
                costs[nv] = c + nc
                heapq.heappush(q, (c + nc, nv))

    # 최단거리 경로 삭제
    q = deque()
    q.append((costs[end], end))

    while q:
        c, v = q.popleft()
        for pc, pv in backprop[v]:
            if costs[pv] + pc == c and (pc, v) in graph[pv]:
                graph[pv].remove((pc, v))
                q.append((c - pc, pv))

    # 두번째 다익스트라
    q = [(0, start)]
    costs = [float("inf")] * N
    costs[start] = 0

    while q:
        c, v = heapq.heappop(q)
        for nc, nv in graph[v]:
            if c + nc < costs[nv]:
                costs[nv] = c + nc
                heapq.heappush(q, (c + nc, nv))

    print(costs[end] if costs[end] != float("inf") else -1)
