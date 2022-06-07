# 용돈 관리

import sys

input = sys.stdin.readline

M, N = map(int, input().split())
money = []
for _ in range(M):
    money.append(int(input()))
print(max(money))
