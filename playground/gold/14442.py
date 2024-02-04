# 벽 부수고 이동하기 2

"""
벽을 부순 횟수를 visited에 기록
벽을 부순 횟수가 더 적은 경우만 이동
"""

import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())

_map = [list(map(int, list(input().strip()))) for _ in range(N)]


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

in_range = lambda y, x: 0 <= y < N and 0 <= x < M

# visited[n] -> 벽을 부수고 이동한 횟수
visited = [[float("inf") for _ in range(M)] for _ in range(N)]

queue = deque()
queue.append((0, 0, 1, 0))  # row, col, 이동한 횟수, 벽을 부순 횟수

ans = float("inf")

while queue:
    y, x, move, wall = queue.popleft()

    if y == N - 1 and x == M - 1:
        ans = min(ans, move)
        continue

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if in_range(ny, nx):
            nwall = wall if _map[ny][nx] == 0 else wall + 1

            # 벽을 부수고 이동한 횟수가 더 적을 때만 이동
            if nwall <= K and nwall < visited[ny][nx]:
                visited[ny][nx] = nwall
                queue.append((ny, nx, move + 1, nwall))

print(ans if ans != float("inf") else -1)
