# 운동

"""
1. 플로이드-워셜 알고리즘으로 모든 정점 사이의 거리를 구한다.
2. 정점마다 다음을 수행한다.
2-1 인접한 노드까지의 거리와 그로부터 자기 자신까지의 거리를 구한다.
2-2 위에서 구한 값 중 최솟값을 찾는다.
"""

import sys

input = sys.stdin.readline

V, E = map(int, input().split())

# graph[a][b] -> a에서 b까지의 거리
graph = [[float("inf")] * (V + 1) for _ in range(V + 1)]
for x in range(1, V + 1):
    graph[x][x] = 0

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, V + 1):
    for a in range(1, V + 1):
        for b in range(1, V + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

ans = float("inf")

for a in range(1, V + 1):
    for b in range(1, V + 1):
        if a != b and graph[a][b] != float("inf"):
            ans = min(ans, graph[a][b] + graph[b][a])

print(ans if ans != float("inf") else -1)
