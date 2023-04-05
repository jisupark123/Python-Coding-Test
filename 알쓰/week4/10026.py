# 적록색약

import sys

sys.setrecursionlimit(1000000)

input = sys.stdin.readline

N = int(input())
area1 = []
area2 = []

for _ in range(N):
    lst1 = []
    lst2 = []
    for s in list(input().strip()):
        lst1.append(s)
        if s == "G":
            lst2.append("R")
        else:
            lst2.append(s)
    area1.append(lst1)
    area2.append(lst2)

direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]


visit = [[False for _ in range(N)] for _ in range(N)]
res1 = 0


def dfs1(color, i, j):
    for d in direction:
        next_i = i + d[0]
        next_j = j + d[1]
        if (
            0 <= next_i < N
            and 0 <= next_j < N
            and not visit[next_i][next_j]
            and area1[next_i][next_j] == color
        ):
            visit[next_i][next_j] = True
            dfs1(color, next_i, next_j)


for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            dfs1(area1[i][j], i, j)
            res1 += 1

########################################################


visit = [[False for _ in range(N)] for _ in range(N)]
res2 = 0


def dfs2(color, i, j):
    for d in direction:
        next_i = i + d[0]
        next_j = j + d[1]
        if (
            0 <= next_i < N
            and 0 <= next_j < N
            and not visit[next_i][next_j]
            and area2[next_i][next_j] == color
        ):
            visit[next_i][next_j] = True
            dfs2(color, next_i, next_j)


for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            dfs2(area2[i][j], i, j)
            res2 += 1


print(res1, res2)
