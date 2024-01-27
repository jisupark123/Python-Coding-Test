# 돌 게임 3

"""
1 O
2 X
3 O
4 O
5 O
6 O
7 X
8 O
9 X
10 O
11 O
12 O
13 O
14 X
15 O
16 X

"""

N = int(input())

dp = [0] * 1001
dp[0] = 0
dp[1] = 1
dp[2] = 0
dp[3] = 1
dp[4] = 1

for i in range(5, 1001):
    if [dp[i - x] for x in (1, 3, 4)].count(0) == 0:
        dp[i] = 0
    else:
        dp[i] = 1

print("SK" if dp[N] == 1 else "CY")
