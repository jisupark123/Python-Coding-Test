# 가장 긴 증가하는 부분 수열

"""
f(n)
-> n을 선택했을 때, n부터 가장 긴 증가하는 부분 수열
-> 1 + max of |오른쪽에서 n보다 큰 수들(n^)의 f(n^)|
"""

N = int(input())

nums = list(map(int, input().split()))


dp = [1] * N

# nums[i]를 시작값으로 가지는 가장 긴 증가하는 부분 수열
for i in range(N - 1, -1, -1):
    for j in range(i + 1, N):
        if nums[i] < nums[j]:
            dp[i] = max(dp[i], 1 + dp[j])

# nums[i]를 마지막값으로 가지는 가장 긴 증가하는 부분 수열
# for i in range(1, N):
#     for j in range(i):
#         if nums[i] > nums[j]:
#             dp[i] = max(dp[i], 1 + dp[j])

print(max(dp))
