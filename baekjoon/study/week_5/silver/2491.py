# 수열


N = int(input())
nums = list(map(int, input().split()))

up_sequence = [1] * (len(nums))
down_sequence = [1] * (len(nums))

for i in range(1, len(nums)):
    if nums[i - 1] < nums[i]:
        up_sequence[i] = up_sequence[i - 1] + 1
    elif nums[i - 1] > nums[i]:
        down_sequence[i] = down_sequence[i - 1] + 1
    else:
        up_sequence[i] = up_sequence[i - 1] + 1
        down_sequence[i] = down_sequence[i - 1] + 1

up_max = max(up_sequence)
down_max = max(down_sequence)
print(max([up_max, down_max]))
