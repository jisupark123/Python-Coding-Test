# 로프

import sys

input = sys.stdin.readline

N = int(input())
ropes = []
for _ in range(N):
    ropes.append(int(input()))
ropes = sorted(ropes, reverse=True)

answer = []

for i in range(N):
    answer.append(ropes[i] * (i + 1))
print(max(answer))
