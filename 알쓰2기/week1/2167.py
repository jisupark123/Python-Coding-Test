# 2차원 배열의 합

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(N)]

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    print(sum([sum(lst[a][j - 1 : y]) for a in range(i - 1, x)]))
