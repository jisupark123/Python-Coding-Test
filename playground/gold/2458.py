# 키 순서

"""
1. 플로이드-워셜 알고리즘으로 각 학생간 거리를 구한다.
2. 단방향 그래프이므로 거리가 존재한다는 것은 나보다 더 크다는 것이다.
3. 각 학생마다 작은 학생과 큰 학생의 숫자를 구해서 2개의 합이 N-1이라면 답에 추가
"""

import sys

input = sys.stdin.readline


N, M = map(int, input().split())

# graph[a][b] -> inf가 아니라면 a보다 키가 큰 것
graph = [[float("inf")] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1


for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

taller = [0] * (N + 1)  # taller[n] -> n보다 큰 사람 수
smaller = [0] * (N + 1)  # smaller[n] -> n보다 작은 사람 수

for a in range(1, N + 1):
    for b in range(1, N + 1):
        if graph[a][b] != float("inf"):
            taller[a] += 1
            smaller[b] += 1

ans = 0

for x in range(1, N + 1):
    if taller[x] + smaller[x] == N - 1:
        ans += 1

print(ans)
