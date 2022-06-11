# 나머지

nums = [int(input()) for _ in range(10)]
nums = list(map(lambda x: x % 42, nums))
print(len(set(nums)))
