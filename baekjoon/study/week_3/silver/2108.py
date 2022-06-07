# 통계학


import sys

input = sys.stdin.readline


# 산술평균
def get_average(nums):
    return round(sum(nums) / len(nums))


# 중앙값
def get_middle_value(nums):
    return nums[len(nums) // 2]


# 최빈값
def get_many_num(nums):
    if len(nums) == 1:
        return nums[0]
    count = {}
    for num in nums:
        try:
            count[num] += 1
        except:
            count[num] = 1
    max_key = []
    max_count = 0
    for key in count:
        if count[key] > max_count:
            max_key = [key]
            max_count = count[key]
        elif count[key] == max_count:
            max_key.append(key)

    return max_key[0] if len(max_key) == 1 else sorted(max_key)[1]


# 범위
def get_range(nums):
    return max(nums) - min(nums)


N = int(input())

nums = [int(input()) for _ in range(N)]
nums.sort()

print(get_average(nums))
print(get_middle_value(nums))
print(get_many_num(nums))
print(get_range(nums))
