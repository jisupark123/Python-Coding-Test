"""
1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    1.바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
    2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우, 
    1. 반시계 방향으로 90도 회전한다.
    2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
    3. 1번으로 돌아간다.
"""

import sys

input = sys.stdin.readline

TOP = 0
RIGHT = 1
BOTTOM = 2
LEFT = 3

dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

N, M = map(int, input().split())
r, c, d = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(N)]
# visited = [[] * M for _ in range(N)]
# visited[r][c].append(d)


def get_back_coordinate():
    if d == TOP:
        return (r + 1, c)
    if d == RIGHT:
        return (r, c - 1)
    if d == BOTTOM:
        return (r - 1, c)
    return (r, c + 1)


def get_front_coordinate():
    if d == TOP:
        return (r - 1, c)
    if d == RIGHT:
        return (r, c + 1)
    if d == BOTTOM:
        return (r + 1, c)
    return (r, c - 1)


# 반시계 방향으로 회전한 값을 반환
def rotated(d):
    if d == TOP:
        return LEFT
    if d == LEFT:
        return BOTTOM
    if d == BOTTOM:
        return RIGHT
    return TOP


res = 0

while True:
    # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if _map[r][c] == 0:
        _map[r][c] = 2
        res += 1

    is_near_clean = True
    for i in range(4):
        ny, nx = r + dy[i], c + dx[i]
        if 0 <= ny < N and 0 <= nx < M and _map[ny][nx] == 0:
            is_near_clean = False
    # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    if is_near_clean:
        back = get_back_coordinate()
        # 1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
        if 0 <= back[0] < N and 0 <= back[1] < M and _map[back[0]][back[1]] != 1:
            r, c = back

        # 2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
        else:
            print(res)
            break

    else:
        # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,

        # 1. 반시계 방향으로 90도 회전한다.
        d = rotated(d)

        # 2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
        front = get_front_coordinate()
        if 0 <= front[0] < N and 0 <= front[1] < M and _map[front[0]][front[1]] == 0:
            r, c = front

        # 3. 1번으로 돌아간다.
