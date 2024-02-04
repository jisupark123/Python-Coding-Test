# 벽 부수고 이동하기 3


import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())

_map = [list(map(int, list(input().strip()))) for _ in range(N)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

in_range = lambda y, x: 0 <= y < N and 0 <= x < M


# visited[y][x][i] -> 좌표 y,x에서 벽 부수기 남은 횟수가 i일 때 최소 이동 횟수
visited = [[[float("inf")] * (K + 1) for _ in range(M)] for _ in range(N)]
visited[0][0][K] = 0

queue = deque()

# row, col, 이동한 횟수, 벽 부시기 남은 횟수
queue.append((0, 0, 1, K))

ans = float("inf")

while queue:
    y, x, move, wall_left = queue.popleft()

    if y == N - 1 and x == M - 1:
        ans = min(ans, move)
        continue

    is_afternoon = move % 2  # 낮인지

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        nmove = move + 1

        if in_range(ny, nx):

            # 이동하려는 곳이 벽이 아닐 때
            if _map[ny][nx] == 0 and visited[ny][nx][wall_left] > nmove:
                visited[ny][nx][wall_left] = nmove
                queue.append((ny, nx, nmove, wall_left))

            # 이동하려는 곳이 벽일 때
            if (
                _map[ny][nx] == 1
                and wall_left
                and visited[ny][nx][wall_left - 1] > nmove
            ):
                if is_afternoon:
                    visited[ny][nx][wall_left - 1] = nmove
                    queue.append((ny, nx, nmove, wall_left - 1))
                else:
                    queue.append((y, x, nmove, wall_left))


print(ans if ans != float("inf") else -1)
