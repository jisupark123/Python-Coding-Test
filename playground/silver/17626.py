n = int(input())

dp = [4] * (n + 1)  # dp[i] -> i를 제곱수로 표현하는 최소 횟수
dp[0] = 0
dp[1] = 1

for i in range(n):
    for j in range(1, n):
        multi_j = j**2
        if i + multi_j > n:
            break
        if dp[i + multi_j] == 0:
            dp[i + multi_j] = dp[i] + 1
        else:
            dp[i + multi_j] = min(dp[i + multi_j], dp[i] + 1, 4)

print(dp[n])
