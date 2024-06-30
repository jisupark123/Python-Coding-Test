# 욕심쟁이 판다

"""
f(i,j)
-> i행 j열에서 움직일 수 있는 최대 칸 개수
-> 인접한 4곳 중 i,j보다 큰 곳의 max + 1
-> 위치별로 정렬해서 큰 숫자를 가진 좌표순으로 구한다.
"""

import sys

input = sys.stdin.readline

N = int(input())
forest = [list(map(int, input().split())) for _ in range(N)]

sorting = []
for i in range(N):
    for j in range(N):
        sorting.append((forest[i][j], i, j))

sorting.sort(reverse=True)
# sorting = [(x[1], x[2]) for x in sorting]

dp = [[1] * N for _ in range(N)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

for _, y, x in sorting:
    for a in range(4):
        ny = y + dy[a]
        nx = x + dx[a]
        if 0 <= ny < N and 0 <= nx < N and forest[ny][nx] > forest[y][x]:
            dp[y][x] = max(dp[y][x], dp[ny][nx] + 1)

print(max((max(x) for x in dp)))
