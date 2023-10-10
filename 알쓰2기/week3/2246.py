# 콘도 선정

import sys

input = sys.stdin.readline

N = int(input())

condo = sorted([list(map(int, input().split())) for _ in range(N)])
cost = 1e9
res = 0
for d, c in condo:
    if c < cost:
        cost = c
        res += 1
print(res)
