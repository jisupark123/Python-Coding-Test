# 영역 구하기

import sys

sys.setrecursionlimit(100000000)

input = sys.stdin.readline

m, n, k = map(int, input().split())

# 종이
paper = [[0 for _ in range(n)] for _ in range(m)]

# 방문 처리
visited = [[False for _ in range(n)] for _ in range(m)]
res = []

# 종이에 색칠하기
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            paper[y][x] = 1


def dfs(y, x):
    res = 0

    def _dfs(y, x):
        nonlocal res
        res += 1
        visited[y][x] = True
        direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        for d in direction:
            next_step = (y + d[0], x + d[1])
            if (
                0 <= next_step[0] < m
                and 0 <= next_step[1] < n
                and paper[next_step[0]][next_step[1]] == 0
                and not visited[next_step[0]][next_step[1]]
            ):
                _dfs(next_step[0], next_step[1])

    _dfs(y, x)
    return res


# 모든 종이를 숞회하면서 방문처리 되어있지 않은 곳이면 dfs 호출
for y in range(m):
    for x in range(n):
        if paper[y][x] == 0 and not visited[y][x]:
            cnt = dfs(y, x)
            res.append(cnt)

print(len(res))
for num in sorted(res):
    print(num, end=" ")
