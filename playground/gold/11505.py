# 구간 곱 구하기 (세그먼트 트리)

import sys

input = sys.stdin.readline

R = 1000000007

N, M, K = map(int, input().split())

nums = [int(input()) for _ in range(N)]


tree = [0] * (len(nums) * 4)


def init(start, end, idx):

    if start == end:
        tree[idx] = nums[start]
        return tree[idx]

    mid = (start + end) // 2
    tree[idx] = init(start, mid, idx * 2) * init(mid + 1, end, idx * 2 + 1) % R

    return tree[idx]


def interval_mul(start, end, idx, left, right):

    # 범위를 벗어나면
    if left > end or right < start:
        return 1

    # 범위 안에 들어오면
    if left <= start and right >= end:
        return tree[idx]

    mid = (start + end) // 2
    return (
        interval_mul(start, mid, idx * 2, left, right)
        * interval_mul(mid + 1, end, idx * 2 + 1, left, right)
        % R
    )


def update(start, end, idx, node, value):

    # 범위를 벗어나면
    if node < start or node > end:
        return tree[idx]

    # node를 찾으면
    if start == end:
        tree[idx] = value

    else:
        mid = (start + end) // 2
        tree[idx] = (
            update(start, mid, idx * 2, node, value)
            * update(mid + 1, end, idx * 2 + 1, node, value)
            % R
        )

    return tree[idx]


init(0, N - 1, 1)


for _ in range(M + K):
    a, b, c = map(int, input().split())

    if a == 1:
        update(0, N - 1, 1, b - 1, c)
    else:
        print(interval_mul(0, N - 1, 1, b - 1, c - 1))
