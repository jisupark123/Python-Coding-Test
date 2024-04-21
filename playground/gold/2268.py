# 수들의 합 7 (세그먼트 트리)

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

nums = [0] * N

tree = [0] * (N * 4)


def interval_sum(start, end, idx, left, right):

    # 범위 밖에 있는 경우
    if left > end or right < start:
        return 0

    # 범위 안에 있는 경우 (left, right 범위 안에 start, end가 들어온 경우)
    if left <= start and right >= end:
        return tree[idx]

    # 두 부분으로 나누어 합을 구하기
    mid = (start + end) // 2
    return interval_sum(start, mid, idx * 2, left, right) + interval_sum(
        mid + 1, end, idx * 2 + 1, left, right
    )


def update(start, end, idx, node, value):

    # 범위 밖에 있는 경우
    if node < start or node > end:
        return tree[idx]

    # node를 찾은 경우 값 변경
    if start == end:
        tree[idx] = value

    # 아닐 경우 왼쪽과 오른쪽을 더해서 값 변경
    else:
        mid = (start + end) // 2
        tree[idx] = update(start, mid, idx * 2, node, value) + update(
            mid + 1, end, idx * 2 + 1, node, value
        )

    return tree[idx]


for _ in range(M):
    a, b, c = map(int, input().split())

    if a == 0:

        # i < j 라는 보장이 없기 때문에 정렬 후 진행
        print(interval_sum(0, N - 1, 1, *sorted([b - 1, c - 1])))
    else:
        update(0, N - 1, 1, b - 1, c)
