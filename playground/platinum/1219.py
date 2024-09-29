# 오민식의 고민

"""
1. 도착 도시로 오는 모든 도로의 비용(가중치)에서 도착 도시의 보상을 뺀다.
2. 시작지점부터 도착지점까이 최소 비용을 밸만포드 알고리즘으로 구한다.
3. 밸만포드 알고리즘에서 V(정점의 개수)번째에도 최단거리가 갱신되면 음의 사이클 존재
- 이때, 사이클에 해당하는 노드들과 목표 노드가 연결되어 있는지 bfs로 확인 (연결되어 있지 않다면 사이클이 있어도 수익이 무제한이 되지 않는다)

"""

import sys
from collections import deque


def is_connected(a, b):
    visited = [0] * N
    visited[a] = 1
    q = deque()
    q.append(a)

    while q:
        x = q.popleft()
        if x == b:
            return True

        for nx, _ in graph[x]:
            if not visited[nx]:
                visited[nx] = 1
                q.append(nx)

    return False


input = sys.stdin.readline
inf = -float("inf")

N, start, end, M = map(int, input().split())

graph = [[] for _ in range(N)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


rewards = list(map(int, input().split()))


dist = [inf] * N
dist[start] = rewards[start]

cycle = False

for i in range(N):
    for x in range(N):
        for nx, nc in graph[x]:
            if dist[nx] < dist[x] - nc + rewards[nx]:
                dist[nx] = dist[x] - nc + rewards[nx]
                if i == N - 1 and is_connected(x, end):
                    cycle = True


if dist[end] == inf:
    print("gg")
elif cycle:
    print("Gee")
else:
    print(dist[end])
