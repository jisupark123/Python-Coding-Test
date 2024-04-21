# 최솟값

"""
그 지역에서 가장 작은 놈을 구한다.
"""

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

nums = [int(input()) for _ in range(N)]


tree = [0] * (N * 4)


def init(start, end, idx):

    if start == end:
        tree[idx] = nums[start]
        return tree[idx]

    mid = (start + end) // 2
    tree[idx] = min(init(start, mid, idx * 2), init(mid + 1, end, idx * 2 + 1))

    return tree[idx]


def interval_min(start, end, idx, left, right):

    # out of range
    if left > end or right < start:
        return sys.maxsize

    # in of range
    if left <= start and right >= end:
        return tree[idx]

    mid = (start + end) // 2
    return min(
        interval_min(start, mid, idx * 2, left, right),
        interval_min(mid + 1, end, idx * 2 + 1, left, right),
    )


init(0, N - 1, 1)
for _ in range(M):
    a, b = map(int, input().split())
    print(interval_min(0, N - 1, 1, *sorted([a - 1, b - 1])))
