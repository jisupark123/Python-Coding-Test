# 부녀회장이 될 테야

"""
5  1  7  28 84 210
4  1  6  21 56 126
3  1  5  15 35 70
2  1  4  10 20 35
1  1  3  6  10 15
0  1  2  3  4  5            (0층)
   1  2  3  4  5

"""

import sys

input = sys.stdin.readline

T = int(input())


for _ in range(T):
    floor = int(input())
    room = int(input())
    info = [[0 for _ in range(room + 1)] for _ in range(floor + 1)]
    for i in range(room + 1):
        info[0][i] = i
    for f in range(1, floor + 1):
        for r in range(1, room + 1):
            info[f][r] = info[f - 1][r] + info[f][r - 1]
    print(info[floor][room])
