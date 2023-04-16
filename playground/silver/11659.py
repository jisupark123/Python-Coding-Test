# 구간 합 구하기 4

import sys

input = sys.stdin.readline
N, M = map(int, input().split())

lst = map(int, input().split())
prefix_sum = [0]

total = 0
for num in lst:
    total += num
    prefix_sum.append(total)


for _ in range(M):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a - 1])
