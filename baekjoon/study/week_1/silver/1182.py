# 부분수열의 합

import sys
from itertools import combinations

N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

answer = 0
for n in range(1, N + 1):
    for i in combinations(nums, n):
        if sum(i) == S:
            answer += 1

print(answer)
