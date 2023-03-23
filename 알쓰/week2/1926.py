# 그림
import sys

sys.setrecursionlimit(10000000)
input = sys.stdin.readline


N, M = map(int, input().split())
picture = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]


def dfs(cnt, n, m):

    total = 0

    def _dfs(cnt, n, m):
        visited[n][m] = True
        nonlocal total
        total += 1
        for d in direction:
            next_n = n + d[0]
            next_m = m + d[1]
            if (
                0 <= next_n < N
                and 0 <= next_m < M
                and picture[next_n][next_m] == 1
                and not visited[next_n][next_m]
            ):
                _dfs(cnt + 1, next_n, next_m)

    _dfs(cnt, n, m)
    return total


res = []
for n in range(N):
    for m in range(M):
        if not visited[n][m] and picture[n][m] == 1:
            res.append(dfs(1, n, m))
if len(res) == 0:
    print(0)
    print(0)
else:
    print(len(res))
    print(max(res))
