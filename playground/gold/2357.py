# 최솟값과 최댓값

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

nums = [int(input()) for _ in range(N)]

tree_max = [0] * (N * 4)
tree_min = [0] * (N * 4)


def init(start, end, idx, tree, fn):

    if start == end:
        tree[idx] = nums[start]
        return tree[idx]

    mid = (start + end) // 2
    tree[idx] = fn(
        init(start, mid, idx * 2, tree, fn), init(mid + 1, end, idx * 2 + 1, tree, fn)
    )

    return tree[idx]


def interval_calc(start, end, idx, left, right, tree, fn):
    # out of range
    if left > end or right < start:
        return sys.maxsize if fn == min else -sys.maxsize

    # in of range
    if left <= start and right >= end:
        return tree[idx]

    mid = (start + end) // 2
    return fn(
        interval_calc(start, mid, idx * 2, left, right, tree, fn),
        interval_calc(mid + 1, end, idx * 2 + 1, left, right, tree, fn),
    )


init(0, N - 1, 1, tree_max, max)  # max tree
init(0, N - 1, 1, tree_min, min)  # min tree

for _ in range(M):
    a, b = map(int, input().split())
    _min = interval_calc(0, N - 1, 1, *sorted([a - 1, b - 1]), tree_min, min)
    _max = interval_calc(0, N - 1, 1, *sorted([a - 1, b - 1]), tree_max, max)
    print(_min, _max)
