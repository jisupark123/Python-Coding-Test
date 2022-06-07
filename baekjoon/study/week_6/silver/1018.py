# 체스판 다시 칠하기

import sys


def count_recolor(b):
    res = 1e9
    board = ""
    for i in b:
        board += i
    for start_color in ("W", "B"):
        color = start_color
        count = 0
        for i in range(len(board)):
            if board[i] != color:
                count += 1
            if (i + 1) % 8 != 0:
                color = "W" if color == "B" else "B"
        res = min(res, count)

    return res


input = sys.stdin.readline

N, M = map(int, input().split())

board = [input().strip() for _ in range(N)]
min_recolor = 1e9

for row in range(N - 7):
    for col in range(M - 7):
        new_board = list(map(lambda x: x[col : col + 8], board[row : row + 8]))
        min_recolor = min(min_recolor, count_recolor(new_board))


print(min_recolor)
