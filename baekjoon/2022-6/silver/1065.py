# 한수


def is_hansu(num):
    if num < 100:
        return True
    nums = list(str(num))
    nums = list(map(int, nums))
    gap = nums[0] - nums[1]
    for i in range(1, len(nums)):
        if nums[i - 1] - nums[i] != gap:
            return False

    return True


N = int(input())
res = 0
for num in range(1, N + 1):
    if is_hansu(num):
        res += 1

print(res)
