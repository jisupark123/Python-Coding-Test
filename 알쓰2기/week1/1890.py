# 점프

import sys


input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().strip().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1  # 초기 값

# 반복문을 통해 갈 수 있는 그래프의 좌표를 탐색
for i in range(N):
    for j in range(N):
        # 현재 탐색하는 좌표가 오른쪽 맨 끝 점이면 반복을 멈춘다.
        if i == N - 1 and j == N - 1:
            print(dp[i][j])
            break

        # 오른쪽으로 이동
        if j + board[i][j] < N:
            dp[i][j + board[i][j]] += dp[i][j]

        # 아래로 이동
        if i + board[i][j] < N:
            dp[i + board[i][j]][j] += dp[i][j]
