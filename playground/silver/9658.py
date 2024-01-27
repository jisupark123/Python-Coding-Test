# 돌 게임 3

"""
1 X
2 O
3 X
4 O
5 O
6 O
7 O
8 X
9 O
10 X
11 O
12 O
13 O
14 O
15 X
16 O
17 X

"""

N = int(input())

dp = [0] * 1001
dp[1] = 0
dp[2] = 1
dp[3] = 0
dp[4] = 1

for i in range(5, 1001):
    if [dp[i - x] for x in (1, 3, 4)].count(0) == 0:
        dp[i] = 0
    else:
        dp[i] = 1

print("SK" if dp[N] == 1 else "CY")
