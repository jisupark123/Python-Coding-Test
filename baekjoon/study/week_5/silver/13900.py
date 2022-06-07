# 순서쌍의 곱의 합

from itertools import combinations


N = int(input())
nums = list(map(int, input().split()))
# combis = list(combinations(nums, 2))
# res = sum(map(lambda x: x[0] * x[1], combis))
# print(res)

sum_nums = sum(nums)
res = 0

for n in nums:
    sum_nums -= n
    res += sum_nums * n

print(res)
