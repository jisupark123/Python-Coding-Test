# 계단 오르기

import sys

input = sys.stdin.readline
arr = []
dp = []
l = int(input())
for _ in range(l):
    arr.append(int(input()))
dp.append(arr[0])
dp.append(max(arr[0] + arr[1], arr[1]))
dp.append(max(arr[0] + arr[2], arr[1] + arr[2]))
for i in range(3, l):
    dp.append(max(dp[i - 2] + arr[i], dp[i - 3] + arr[i] + arr[i - 1]))
print(dp.pop())


# import sys

# input = sys.stdin.readline

# stairs = int(input()) - 1
# steps = []
# for _ in range(stairs + 1):
#     steps.append(int(input()))

# max_num = 0


# def dfs(idx, total, sequence):
#     global max_num
#     if idx == stairs:
#         max_num = max(total, max_num)
#         return
#     try:
#         # 한계단 오를 때
#         if sequence != 2:
#             dfs(idx + 1, total + steps[idx + 1], sequence + 1)
#         # 두계단 오를 때
#         dfs(idx + 2, total + steps[idx + 2], sequence=1)
#     except:
#         return


# dfs(0, steps[0], 1)
# print(max_num)
