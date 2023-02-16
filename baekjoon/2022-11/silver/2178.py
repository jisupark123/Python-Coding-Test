# 미로 탐색


def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return
    for d in directions:
        if (
            0 <= x + d[0] < n
            and 0 <= y + d[1] < m
            and maze[x + d[0]][y + d[1]] == "1"
            and (dp[x + d[0]][y + d[1]] == 0 or dp[x + d[0]][y + d[1]] > dp[x][y] + 1)
        ):
            dp[x + d[0]][y + d[1]] = dp[x][y] + 1
            dfs(x + d[0], y + d[1])


def bfs():
    queue: deque[list[int]] = deque()
    queue.append([0, 0])
    while len(queue) != 0:
        indices = queue.popleft()
        for d in directions:
            if (
                0 <= indices[0] + d[0] < n
                and 0 <= indices[1] + d[1] < m
                and maze[indices[0] + d[0]][indices[1] + d[1]] == "1"
                and (
                    dp[indices[0] + d[0]][indices[1] + d[1]] == 0
                    or dp[indices[0] + d[0]][indices[1] + d[1]]
                    > dp[indices[0]][indices[1]] + 1
                )
            ):
                dp[indices[0] + d[0]][indices[1] + d[1]] = (
                    dp[indices[0]][indices[1]] + 1
                )
                queue.append([indices[0] + d[0], indices[1] + d[1]])


from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split())
maze = [input().strip() for _ in range(n)]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

dp = [[0 for _ in range(m)] for _ in range(n)]
dp[0][0] = 1

bfs()
print(dp[n - 1][m - 1])
