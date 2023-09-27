# 알파벳

"""

"""

import sys

input = sys.stdin.readline

r, c = map(int, input().split())

board = [list(map(lambda x: ord(x) - 65, input().strip())) for _ in range(r)]

visited = [False] * 26
visited[board[0][0]] = True
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

res = 0


def dfs(row, col, cnt):
    moved = False
    for i in range(4):
        next_r, next_c = row + dx[i], col + dy[i]
        if 0 <= next_r < r and 0 <= next_c < c and not visited[board[next_r][next_c]]:
            moved = True
            visited[board[next_r][next_c]] = True
            dfs(next_r, next_c, cnt + 1)
            visited[board[next_r][next_c]] = False

    if not moved:
        global res
        res = max(res, cnt)


dfs(0, 0, 1)
print(res)
