# 로봇 조종하기

"""
i - 행
j - 열
p - 직전 위치 (위/왼쪽/오른쪽)

f(i, j, p)
-> i행 j열에 위치해있고 직전에 p 방향에서 왔을 때 얻을 수 있는 최대 value

f(i, j, up) = max(f(i, j, left), f(i, j-1, right))
f(i, j, left) = max(f(i+1, j, up), f(i, j+1, left))
f(i, j, right) = max(f(i+1, j, up), f(i, j-1, right))

위처럼 dp를 3차원으로 구성해서 dfs 돌리면 시간초과.


f(i, j)
-> i행 j열까지 얻을 수 있는 최댓값
-> 직전에 위/왼쪽/오른쪽 방향에서 온 값 중 최댓값

-> 첫 행은 왼쪽에서 올 수 밖에 없으므로 직접 구해주고 행마다 왼쪽/오른쪽에서 온 값들을 구하고 둘을 비교한다.
"""

import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

N, M = map(int, input().split())

dp = [list(map(int, input().split())) for _ in range(N)]

# 첫번째 행 -> 왼쪽에서 오는 경우만

for i in range(1, M):
    dp[0][i] += dp[0][i - 1]

# 나머지 행 -> 위/왼쪽/오른쪽에서 오는 경우 모두 비교
for i in range(1, N):
    left_to_right = dp[i][:]
    right_to_left = dp[i][:]

    left_to_right[0] += dp[i - 1][0]
    for j in range(1, M):
        left_to_right[j] += max(dp[i - 1][j], left_to_right[j - 1])

    right_to_left[M - 1] += dp[i - 1][M - 1]
    for j in range(M - 2, -1, -1):
        right_to_left[j] += max(dp[i - 1][j], right_to_left[j + 1])

    for j in range(M):
        dp[i][j] = max(left_to_right[j], right_to_left[j])

print(dp[N - 1][M - 1])
