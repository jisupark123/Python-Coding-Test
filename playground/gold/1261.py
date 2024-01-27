# 알고스팟

import sys
import heapq

input = sys.stdin.readline
M, N = map(int, input().split())

maze = [list(map(int, list(input().strip()))) for _ in range(N)]


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

table = [[float("inf")] * M for _ in range(N)]  # 벽을 몇개 부쉈는지
table[0][0] = 0
queue = []
queue.append((0, 0, 0))  # 벽을 부순 횟수, y, x

while queue:
    cnt, y, x = heapq.heappop(queue)
    if y == N - 1 and x == M - 1:
        print(cnt)
        break

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        ncnt = cnt
        if 0 <= ny < N and 0 <= nx < M:
            if maze[ny][nx] == 1:
                ncnt += 1
            if table[ny][nx] > ncnt:  # 벽을 덜 부쉈다면
                table[ny][nx] = ncnt
                heapq.heappush(queue, (ncnt, ny, nx))
