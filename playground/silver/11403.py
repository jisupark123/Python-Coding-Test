# 경로 찾기

import sys

input = sys.stdin.readline
N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):  # 중간노드 설정
    for i in range(N):
        for j in range(N):
            if graph[i][k] == 1 and graph[k][j] == 1:  # k를 중간다리로 놓고 i와 j가 연결되는지
                graph[i][j] = 1

for g in graph:
    print(*g)
