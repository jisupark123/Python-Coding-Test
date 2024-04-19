# 파일 합치기

"""
x 인덱스부터 y 인덱스까지의 최소 비용

f(x, y) = min of | f(x, x) + f(x+1, y) + sum(x~y), f(x, x+1) + f(x+2, y) + sum(x~y), ... , f(x, y-1) + f(y, y) + sum(x~y)
"""

import sys

input = sys.stdin.readline

for _ in range(int(input())):

    N = int(input())

    files = list(map(int, input().split()))

    # sum(files[a:b])
    def acc_sum(a, b):
        if a == 0:
            return acc_files[b - 1]

        return acc_files[b - 1] - acc_files[a - 1]

    acc_files = [files[0]]

    for i in range(1, N):
        acc_files.append(acc_files[-1] + files[i])

    dp = [[0] * N for _ in range(N)]

    for i in range(N - 1):
        dp[i][i + 1] = files[i] + files[i + 1]

    for n in range(2, N):
        for x in range(N - n):
            y = x + n

            dp[x][y] = min(
                (dp[x][i] + dp[i + 1][y] + acc_sum(x, y + 1) for i in range(x, y))
            )

    print(dp[0][N - 1])
