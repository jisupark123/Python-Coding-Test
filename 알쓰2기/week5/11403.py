# 경로 찾기

import sys

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for a in range(N):
        for b in range(N):
            if graph[a][k] == 1 and graph[k][b] == 1:
                graph[a][b] = 1

for g in graph:
    print(*g)
