# 뱀

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
K = int(input())

EMPTY = -1
APPLE = 5
SNAKE = 6
LEFT = 0
TOP = 1
RIGHT = 2
BOTTOM = 3

# ← ↑ → ↓
direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]

board = [[EMPTY for _ in range(N)] for _ in range(N)]
board[0][0] = SNAKE

for _ in range(K):
    apple = map(int, input().split())
    board[next(apple) - 1][next(apple) - 1] = APPLE

L = int(input())

dir_changes = [input().strip().split() for _ in range(L)]


# 뱀이 회전하면 방향을 고치는 함수
def get_next_direction(rotate, curr_dir):
    next_dir = curr_dir
    if rotate == "L":  # 왼쪽으로 90도 회전
        next_dir -= 1
    else:  # "D", 오른쪽으로 90도 회전
        next_dir += 1
    if next_dir == -1:
        next_dir = 3
    elif next_dir > 3:
        next_dir = 0

    return next_dir


sec = 0  # 게임 시작 후 몇 초 지났는지
curr_dir = RIGHT  # 현재 진행 방향 (dir_changes[2] 오른쪽)
curr_idx = (0, 0)
i = 0  # dir_changes 인덱스

prev_moves = deque([(0, 0)])  # 이전의 move들 저장


while True:
    if i < L and sec == int(dir_changes[i][0]):  # 방향 회전 여부
        curr_dir = get_next_direction(dir_changes[i][1], curr_dir)
        i += 1

    next_idx = (
        curr_idx[0] + direction[curr_dir][0],
        curr_idx[1] + direction[curr_dir][1],
    )

    if (
        # next_idx[0] + direction[curr_dir][0] == -1
        # or next_idx[0] + direction[curr_dir][0] == N
        # or next_idx[1] + direction[curr_dir][1] == -1
        # or next_idx[1] + direction[curr_dir][1] == N
        0 > next_idx[0]
        or N <= next_idx[0]
        or 0 > next_idx[1]
        or N <= next_idx[1]
        or board[next_idx[0]][next_idx[1]] == SNAKE
    ):
        print(sec + 1)

        break
    if board[next_idx[0]][next_idx[1]] != APPLE:
        prev_move = prev_moves.popleft()
        board[prev_move[0]][prev_move[1]] = EMPTY

    board[next_idx[0]][next_idx[1]] = SNAKE
    curr_idx = next_idx
    prev_moves.append(next_idx)
    sec += 1
