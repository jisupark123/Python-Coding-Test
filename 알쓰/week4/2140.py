# 지뢰찾기

"""
각 칸은 지뢰(-2)거나 지뢰가 아니다(-3)
만약 
"""

import sys

input = sys.stdin.readline

N = int(input())

board = []
empty = []

for i in range(N):
    row = []
    _input = input().strip()
    for j in range(N):
        if _input[j] == "#":
            empty.append([i, j])
            row.append(-1)
        else:
            row.append(int(_input[j]))
    board.append(row)
