# 줄 세우기


N = int(input())
nums = list(map(int, input().split()))
res = []
for i in range(len(nums)):
    if i - nums[i] == len(res):
        res.append(i + 1)
    else:
        res.insert(i - nums[i], i + 1)
print(*res)
