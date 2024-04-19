# 타일 채우기

"""
3xN 크기의 벽을 2x1, 1x2 크기의 타일로 채우는 경우의 수 

- f(n)
- 2x1 타일을 차곡차곡 채웠을 때, n개를 채우는 경우의 수
- if (2 * n) % 3 == 0 -> f(n-1) + f(n-2) + f(n-3)
- if (2 * n) % 3 == 1 -> f(n-1)
- if (2 * n) % 3 == 2 -> f(n-1) + f(n-2)
"""

N = int(input())

if N % 2 == 1:
    print(0)
    exit(0)

dp = [0] * (max(3, 3 * N // 2) + 1)
dp[1] = 1
dp[2] = 1
dp[3] = 3

for n in range(4, len(dp)):
    if (2 * n) % 3 == 0:
        dp[n] = dp[n - 1] + dp[n - 2] + dp[n - 3]
    elif (2 * n) % 3 == 1:
        dp[n] = dp[n - 1]
    else:
        dp[n] = dp[n - 1] + dp[n - 2]

print(dp[3 * N // 2])
