# 좋다


"""
key가 숫자의 합, value가 [인덱스,인덱스] 형식의 리스트
key가 존재하고 value의 조합 중에 해당 숫자의 인덱스가 포함되지 않은 조합이 있다면 '좋다'
"""

from collections import defaultdict

N = int(input())

nums = list(map(int, input().split()))
num_combi = defaultdict(list)

max_num = max(nums)

for i in range(N):
    for j in range(i + 1, N):
        if nums[i] + nums[j] <= max_num:  # 최적화 (속도, 메모리 초과)
            num_combi[nums[i] + nums[j]].append((i, j))

count = 0

for i in range(N):
    if len(num_combi[nums[i]]) == 0:
        continue
    for combi in num_combi[nums[i]]:
        if i not in combi:
            count += 1
            break

print(count)
