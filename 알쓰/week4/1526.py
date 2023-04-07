# 가장 큰 금민수

N = int(input())

limit = 1000001

dp = [False] * limit


def dfs(s):
    if int(s) > limit:
        return
    dp[int(s)] = True
    if int(s + "4") <= limit and dp[int(s + "4")] == False:
        dfs(s + "4")
    if int(s + "7") <= limit and dp[int(s + "7")] == False:
        dfs(s + "7")


dfs("4")
dfs("7")


for i in range(N, 0, -1):
    if dp[i]:
        print(i)
        break
