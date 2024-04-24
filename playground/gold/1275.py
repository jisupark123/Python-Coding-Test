# 커피숍2

import sys

input = sys.stdin.readline

N, Q = map(int, input().split())

nums = list(map(int, input().split()))


tree = [0] * (len(nums) * 4)


# 세그먼트 트리 초기화
# start : 배열의 시작 인덱스, end : 배열의 마지막 인덱스
# index : 세그먼트 트리의 인덱스 (무조건 1부터 시작)
def init(start, end, idx):
    if start == end:
        tree[idx] = nums[start]
        return tree[idx]

    mid = (start + end) // 2
    tree[idx] = init(start, mid, idx * 2) + init(mid + 1, end, idx * 2 + 1)
    return tree[idx]


# 구간합 구하는 함수
# start, end : 트리 구간합 시작, 끝 인덱스
# left, right : 구간 합을 구하고자 하는 범위
# left, right 범위에 들어오는 start, end를 전부 return
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


# 특정 원소의 값을 수정
# start, end : 트리 구간합 시작, 끝 인덱스
# node : 구간 합을 수정하고자 하는 노드 인덱스
# value : 수정할 값
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


init(0, N - 1, 1)

for _ in range(Q):
    a, b, c, d = map(int, input().split())
    print(interval_sum(0, N - 1, 1, *sorted([a - 1, b - 1])))
    update(0, N - 1, 1, c - 1, d)
