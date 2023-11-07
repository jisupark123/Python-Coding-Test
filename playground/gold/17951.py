# 흩날리는 시험지 속에서 내 평점이 느껴진거야

"""
이분탐색으로 해결
mid를 최대한의 점수로 만드는 탐색을 수행한다.

ans -> 정답을 저장 (최대한의 점수)
start -> 0
end -> 전체 점수의 합

while문으로 탐색, 반복 조건 -> start < end
매 탐색마다 ans를 업데이트
mid가 가능하면 start = mid + 1
불가능하면 end = mid - 1
"""

import sys

input = sys.stdin.readline

N, K = map(int, input().split())

sequence = list(map(int, input().split()))

start = min(sequence)
end = sum(sequence)
ans = start


# x -> 점수
def possible(x):
    group = 0
    tmp = 0
    for score in sequence:
        tmp += score
        if tmp >= x:
            group += 1
            tmp = 0

    return True if group >= K else False


while start <= end:
    mid = (start + end) // 2
    if possible(mid):
        ans = max(ans, mid)
        start = mid + 1
    else:
        end = mid - 1

print(ans)
