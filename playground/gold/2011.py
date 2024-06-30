# 암호코드

"""
dp[i] - i번째까지 고려했을 때 경우의 수
"""

s = input()

dp = [0] * len(s)

if s[0] == "0":
    print(0)
    exit(0)

dp[0] = 1

for i in range(1, len(s)):
    if s[i] != "0":
        dp[i] = dp[i - 1]
    if s[i - 1] != "0" and int(s[i - 1] + s[i]) <= 26:
        if i == 1:
            dp[i] += 1
        else:
            dp[i] += dp[i - 2]

print(dp[-1] % 1000000)
