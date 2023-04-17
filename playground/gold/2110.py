# 공유기 설치

import sys

input = sys.stdin.readline
N, C = map(int, input().split())

lst = [int(input()) for _ in range(N)]
lst.sort()


def simulate(n):
    cnt = 1
    prev = lst[0]
    for i in range(1, N):
        if lst[i] - prev >= n:
            cnt += 1
            prev = lst[i]
    if cnt >= C:
        return True
    return False


if C == 2:
    print(lst[-1] - lst[0])
else:
    res = 1

    start = 1
    end = lst[-1] - lst[0]
    mid = (start + end) // 2
    while start < end:
        mid = (start + end) // 2
        if simulate(mid):
            start = mid + 1
            res = mid
        else:
            end = mid

    print(res)
