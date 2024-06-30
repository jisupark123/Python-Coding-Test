# 가장 긴 바이토닉 부분 수열

"""
가장 긴 증가하는 부분 수열 (LIS) 풀이 응용

i번째 인덱스부터 시작하는 가장 긴 감소하는 부분 수열 +
배열을 거꾸로했을 때 i번째 인덱스부터 시작하는 가장 긴 감소하는 부분 수열의 합이 가장 큰 값이 정답


LIS 점화식
f(n)
-> n을 선택했을 때 n부터의 LIS
-> 1 + max of |오른쪽에서 n보다 큰 수들(n^)의 f(n^)|
"""

N = int(input())
nums = list(map(int, input().split()))

# i번째 인덱스부터 시작하는 가장 긴 감소하는 부분 수열
lis1 = [1] * N
for i in range(N - 1, -1, -1):
    for j in range(i + 1, N):
        if nums[i] > nums[j]:
            lis1[i] = max(lis1[i], 1 + lis1[j])

# 배열을 거꾸로했을 때 i번째 인덱스부터 시작하는 가장 긴 감소하는 부분 수열
nums = nums[::-1]
lis2 = [1] * N
for i in range(N - 1, -1, -1):
    for j in range(i + 1, N):
        if nums[i] > nums[j]:
            lis2[i] = max(lis2[i], 1 + lis2[j])

lis2 = lis2[::-1]

print(max((lis1[i] + lis2[i] for i in range(N))) - 1)
