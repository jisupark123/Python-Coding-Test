# 최댓값

nums = [int(input()) for _ in range(9)]

max_num = 0
idx = 0

for i in range(len(nums)):
    if nums[i] > max_num:
        max_num = nums[i]
        idx = i + 1

print(max_num)
print(idx)
