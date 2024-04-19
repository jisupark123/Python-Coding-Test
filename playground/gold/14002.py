# 가장 긴 증가하는 부분 수열 4

"""
f(n)
-> n을 선택했을 때, n부터 가장 긴 증가하는 부분 수열
-> 1 + max of |오른쪽에서 n보다 큰 수들(n^)의 f(n^)|
"""

N = int(input())

nums = list(map(int, input().split()))


dp = [1] * N

max_i = N - 1

for i in range(N - 1, -1, -1):
    for j in range(i + 1, N):
        if nums[i] < nums[j]:
            dp[i] = max(dp[i], 1 + dp[j])

    if dp[i] > dp[max_i]:
        max_i = i


print(dp[max_i])

ans = [max_i]

for i in range(max_i + 1, N):
    if dp[ans[-1]] - 1 == dp[i]:
        ans.append(i)

print(*list(map(lambda x: nums[x], ans)))
