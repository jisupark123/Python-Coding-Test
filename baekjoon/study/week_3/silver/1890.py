# 점프

import sys

input = sys.stdin.readline

N = int(input())
game_board = [list(map(int, input().split())) for _ in range(N)]


def dp(board, idx, course):
    if board[idx[0]][idx[1]] == 0:
        return
