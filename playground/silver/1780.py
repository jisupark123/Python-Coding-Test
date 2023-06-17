# 종이의 개수

import sys

input = sys.stdin.readline

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

a, b, c = 0, 0, 0


def dfs(row, col, n):
    sample = paper[row][col]
    same_all = True
    for i in range(row, row + n):
        for j in range(col, col + n):
            if sample != paper[i][j]:
                same_all = False
                break
        if not same_all:
            break

    if same_all:
        if sample == -1:
            global a
            a += 1
        elif sample == 0:
            global b
            b += 1
        else:
            global c
            c += 1
    else:
        for i in range(3):
            for j in range(3):
                dfs(row + (i * (n // 3)), col + (j * (n // 3)), n // 3)


dfs(0, 0, N)

print(a)
print(b)
print(c)
