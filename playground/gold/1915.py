# 가장 큰 정사각형

"""
dp[i][j] -> 왼쪽 위로 만들 수 있는 정사각형의 길이
arr[i][j] -> 0 ? dp[i][j] -> 0
dp[i][j] -> min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
"""

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, list(input().strip()))) for _ in range(n)]

dp = [[0] * m for _ in range(n)]

res = 0


for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            dp[i][j] = 0
        else:
            prev_row = 0 if i == 0 else dp[i - 1][j]
            prev_col = 0 if j == 0 else dp[i][j - 1]
            prev_diag = 0 if i == 0 or j == 0 else dp[i - 1][j - 1]
            dp[i][j] = min(prev_row, prev_col, prev_diag) + 1
            res = max(res, dp[i][j])

print(res**2)


# import sys

# input = sys.stdin.readline

# n, m = map(int, input().split())

# arr = [list(map(int, list(input().strip()))) for _ in range(n)]


# def find(x):  # x 크기의 정사각형이 있는지 확인
#     for i in range(n - x + 1):
#         for j in range(m - x + 1):
#             flag = True
#             for a in range(i, i + x):
#                 for b in range(j, j + x):
#                     if arr[a][b] == 0:
#                         flag = False
#                         break
#             if flag:
#                 return True

#     return False


# start = 0
# end = min(n, m)
# res = 0

# while start < end:
#     mid = (start + end) // 2
#     if find(mid):
#         res = mid
#         start = mid + 1
#     else:
#         end = mid - 1

# print(res**2)
