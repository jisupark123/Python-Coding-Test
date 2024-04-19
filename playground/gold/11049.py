# 행렬 곱셈 순서

"""
x 인덱스부터 y 인덱스까지의 최소 비용

f(x, y) = min of | f(x, x) + f(x+1, y) + 행렬곱 비용, f(x, x+1) + f(x+2, y) + 행렬곱 비용, ... , f(x, y-1) + f(y, y) + 행렬곱 비용
"""

import sys

input = sys.stdin.readline

N = int(input())

matrixes = [list(map(int, input().split())) for _ in range(N)]


dp = [[0] * N for _ in range(N)]

for n in range(1, N):
    for x in range(N - n):
        y = x + n

        dp[x][y] = min(
            (
                dp[x][i]
                + dp[i + 1][y]
                + matrixes[x][0] * matrixes[i][1] * matrixes[y][1]
                for i in range(x, y)
            )
        )

print(dp[0][N - 1])
