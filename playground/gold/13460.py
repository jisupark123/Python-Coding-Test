# 구슬 탈출 2

"""
각 차례마다 왼쪽,오른쪽,위쪽,아래쪽 각각으로 기울이는 것을 재귀함수를 돌린다.
"""

import sys

input = sys.stdin.readline

EMPTY = "."
WALL = "#"
HOLE = "O"
RED = "R"
BLUE = "B"
HOLE_IN_ONE = -1
FAIL = -2

N, M = map(int, input().split())

board = [list(input().strip()) for _ in range(N)]

red_start = ()
blue_start = ()

for i in range(N):
    for j in range(M):
        if board[i][j] == RED:
            red_start = (i, j)
            board[i][j] = EMPTY
        elif board[i][j] == BLUE:
            blue_start = (i, j)
            board[i][j] = EMPTY


cnt = 11


def move_to_end(to_y, to_x, row, col, diff_row, diff_col):
    while True:
        if board[row + to_y][col + to_x] == HOLE:
            return HOLE_IN_ONE
        if board[row + to_y][col + to_x] == EMPTY and (
            row + to_y != diff_row or col + to_x != diff_col
        ):
            row += to_y
            col += to_x
        else:
            break
    return (row, col)


# 주어진 방향으로 red,blue 구슬을 옮기고
# blue가 구멍에 빠지면 FAIL을 반환한다.
# red만 구멍에 빠지면 HOLE_IN_ONE을 반환한다.
# 그 외에는 red와 blue의 위치를 반환한다.
def move(direction, red_row, red_col, blue_row, blue_col):
    to_y = 0
    to_x = 0
    red_is_first = True
    if direction == "L":
        to_y = 0
        to_x = -1
        red_is_first = red_col < blue_col
    elif direction == "R":
        to_y = 0
        to_x = 1
        red_is_first = red_col > blue_col
    elif direction == "T":
        to_y = -1
        to_x = 0
        red_is_first = red_row < blue_row
    else:
        to_y = 1
        to_x = 0
        red_is_first = red_row > blue_row

    if red_is_first:
        new_red = move_to_end(to_y, to_x, red_row, red_col, blue_row, blue_col)
        if new_red == HOLE_IN_ONE:
            red_row, red_col = 0, 0
        new_blue = move_to_end(to_y, to_x, blue_row, blue_col, red_row, red_col)
    else:
        new_blue = move_to_end(to_y, to_x, blue_row, blue_col, red_row, red_col)
        if new_blue == HOLE_IN_ONE:
            blue_row, blue_col = 0, 0
        new_red = move_to_end(to_y, to_x, red_row, red_col, blue_row, blue_col)

    if new_blue == HOLE_IN_ONE:
        return FAIL
    if new_red == HOLE_IN_ONE:
        return HOLE_IN_ONE
    if (*new_red, *new_blue) == (red_row, red_col, blue_row, blue_col):
        return FAIL
    return (*new_red, *new_blue)


def dfs(red_row, red_col, blue_row, blue_col, n, prev_d):
    global cnt
    if n >= 10 or n >= cnt:
        return
    for direction in ("T", "R", "B", "L"):
        if direction == prev_d:
            continue
        res = move(direction, red_row, red_col, blue_row, blue_col)
        if res == HOLE_IN_ONE:
            cnt = min(cnt, n + 1)

        elif res != FAIL:
            dfs(*res, n + 1, direction)


dfs(*red_start, *blue_start, 0, "Z")

if cnt <= 10:
    print(cnt)
else:
    print(-1)
