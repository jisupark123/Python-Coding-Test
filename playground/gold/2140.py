# 지뢰찾기

"""
숫자를 모두 조사한다. (빈 칸은 조사할 필요가 없다)
숫자 n의 인접한 칸을 모두 조사한다.

만약 지뢰의 개수가 n과 같다면 인접한 빈칸(-1)을 모두 SAFE(-3)로 바꾼다.
만약 (빈칸(-1)의 개수 + 지뢰(-2)의 개수)가 n과 같다면 빈칸(-1)을 모두 지뢰(-2)로 바꾼다.


조사가 끝나면 보드를 모두 순회하면서 지뢰(-2)와 빈칸(-1)의 개수를 모두 더한 결과를 출력한다.
"""

import sys

input = sys.stdin.readline

UNKNOWN = -1  # 아직 결정되지 않은 곳
MINE = -2  # 지뢰가 있는 곳
SAFE = -3  # 지뢰가 없는 곳

N = int(input())
board = []

# 보드 만들기
for _ in range(N):
    lst = []
    for s in input().strip():
        if s == "#":
            lst.append(UNKNOWN)
        else:
            lst.append(int(s))
    board.append(lst)

# 8방향
# ← ↖ ↑ ↗ → ↘ ↓ ↙
direction = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]


# 숫자 n에 인접한 칸들을 모두 조사한다.
# 만약 지뢰의 개수가 n과 같다면 인접한 빈칸(-1)을 모두 SAFE(-3)로 바꾼다.
# 만약 (빈칸(-1)의 개수 + 지뢰(-2)의 개수)가 n과 같다면 빈칸(-1)을 모두 지뢰(-2)로 바꾼다.
def find_mine(i, j):
    unknown_cnt = 0
    mine_cnt = 0
    for r, c in direction:
        if 0 <= i + r < N and 0 <= j + c < N:
            if board[i + r][j + c] == UNKNOWN:
                unknown_cnt += 1
            elif board[i + r][j + c] == MINE:
                mine_cnt += 1

    if board[i][j] == mine_cnt:
        for r, c in direction:
            if 0 <= i + r < N and 0 <= j + c < N and board[i + r][j + c] == UNKNOWN:
                board[i + r][j + c] = SAFE
    elif board[i][j] == unknown_cnt + mine_cnt:
        for r, c in direction:
            if 0 <= i + r < N and 0 <= j + c < N and board[i + r][j + c] == UNKNOWN:
                board[i + r][j + c] = MINE


for i in range(N):
    for j in range(N):
        if board[i][j] >= 0:
            for r, c in direction:
                if 0 <= i + r < N and 0 <= j + c < N:
                    find_mine(i + r, j + c)

res = 0
for i in range(N):
    for j in range(N):
        if board[i][j] in (MINE, UNKNOWN):
            res += 1


print(res)
