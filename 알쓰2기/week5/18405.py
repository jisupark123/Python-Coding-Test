# 경쟁적 전염

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
test_tube = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

queue = []  # (바이러스 번호, i좌표, j좌표, 경과 시간)

for i in range(N):
    for j in range(N):
        if test_tube[i][j] > 0:
            queue.append((test_tube[i][j], i, j, 0))

queue = deque(sorted(queue))

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


while queue:
    k, i, j, time = queue.popleft()
    if time >= S:
        break
    for a in range(4):
        ni, nj = i + di[a], j + dj[a]
        if 0 <= ni < N and 0 <= nj < N and test_tube[ni][nj] == 0:
            test_tube[ni][nj] = k
            queue.append((k, ni, nj, time + 1))

print(test_tube[X - 1][Y - 1])
