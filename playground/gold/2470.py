# 두 용액

import sys

input = sys.stdin.readline
N = int(input())

lst = sorted(list(map(int, input().split())))


min_diff = float("INF")
ans_1 = 0
ans_2 = 0

for i in range(N):
    start = i + 1
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        tmp = lst[i] + lst[mid]

        if min_diff > abs(tmp):
            min_diff = abs(tmp)
            ans_1 = lst[i]
            ans_2 = lst[mid]

            if tmp == 0:
                break

        if tmp >= 0:
            end = mid - 1
        else:
            start = mid + 1

print(ans_1, ans_2)
