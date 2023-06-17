# 케빈 베이컨의 6단계 법칙

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

INF = 100
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for a in range(N + 1):
    for b in range(N + 1):
        if a == b:
            graph[a][b] = 0


for k in range(N + 1):
    for a in range(N + 1):
        for b in range(N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

min_person = 0
min_cnt = 1e9
for i in range(len(graph)):
    cnt = sum(graph[i][1:])
    if min_cnt > cnt:
        min_cnt = cnt
        min_person = i


print(min_person)
