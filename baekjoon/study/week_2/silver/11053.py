# 가장 긴 증가하는 부분 수열
import sys

input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
res = [1] * N
for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            res[i] = max(res[i], res[j] + 1)

print(max(res))
