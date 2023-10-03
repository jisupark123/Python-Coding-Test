# 2차원 배열의 합

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(N)]

for _ in range(int(input())):
    y1, x1, y2, x2 = map(int, input().split())
    print(sum([sum(lst[i][x1 - 1 : x2]) for i in range(y1 - 1, y2)]))
