# 낚시왕

import sys

input = sys.stdin.readline

TOP = 1
BOTTOM = 2
RIGHT = 3
LEFT = 4

R, C, shark_cnt = map(int, input().split())

# 0 - 빈 칸
# [속력, 이동 방향, 크기]
board = [[0] * C for _ in range(R)]


for _ in range(shark_cnt):
    r, c, s, d, z = map(int, input().split())
    if d in (TOP, BOTTOM):
        s = s % ((R - 1) * 2)
    else:
        s = s % ((C - 1) * 2)
    if r - 1 == 0 and d == TOP:
        d = BOTTOM
    elif r - 1 == R - 1 and d == BOTTOM:
        d = TOP
    elif c - 1 == 0 and d == LEFT:
        d = RIGHT
    elif c - 1 == C - 1 and d == RIGHT:
        d = LEFT
    board[r - 1][c - 1] = [s, d, z]


res = 0


def move(i, j, s, d, z):
    # 이동 후 방향 바꾸기

    n = s
    while n > 0:
        if d == TOP:
            to_move = min(n, i)
            i -= to_move
            n -= to_move
            if i == 0:
                d = BOTTOM
        elif d == BOTTOM:
            to_move = min(n, R - 1 - i)
            i += to_move
            n -= to_move
            if i == R - 1:
                d = TOP
        elif d == LEFT:
            to_move = min(n, j)
            j -= to_move
            n -= to_move
            if j == 0:
                d = RIGHT
        else:
            to_move = min(n, C - 1 - j)
            j += to_move
            n -= to_move
            if j == C - 1:
                d = LEFT

    return (i, j, s, d, z)


for king_pos in range(C):
    # 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다.
    # 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
    for row in range(R):
        if board[row][king_pos] != 0:
            res += board[row][king_pos][2]
            board[row][king_pos] = 0
            break

    # 상어가 이동한다.
    sharks = []
    for i in range(R):
        for j in range(C):
            if board[i][j] != 0:
                sharks.append(move(i, j, *board[i][j]))
                board[i][j] = 0

    for i, j, s, d, z in sharks:
        # 이동한 자리에 다른 물고기가 있다면 둘 중 크기가 작은 물고기 없애기
        if board[i][j] == 0 or board[i][j][2] < z:
            board[i][j] = [s, d, z]


print(res)
