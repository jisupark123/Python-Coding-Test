"""
idea - 하나를 픽하고 이분 탐색으로 차가 최소가 되는 수를 찾는다.

ans_diff, ans_left, ans_right -> 두 용액의 인덱스와 차이의 값을 저장

1. for문을 통해 i번째 수를 픽한다.
2. start,end -> 리스트 시작과 끝 인덱스. mid -> (start+end)//2
3. while 문으로 이분 탐색을 시작한다. 종료 조건 -> start <= end
4. 매 탐색마다 최소 차이의 값(ans_diff)을 업데이트한다.
4. lst[mid] + lst[i] == 0 -> 문제 해결, 종료
5. lst[mid] + lst[i] > 0 -> end = mid + 1 (더 작은 수를 택해야 0에 가까이 다가갈 여지가 있음)
6. lst[mid] + lst[i] < 0 -> start = mid - 1 (더 큰 수를 택해야 0에 가까이 다가갈 여지가 있음)

"""

import sys

input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

ans_diff = float("INF")
ans_left = 0
ans_right = 0

for i in range(N):
    current = lst[i]
    start = i + 1
    end = N - 1

    while start <= end:
        mid = (start + end) // 2
        tmp = current + lst[mid]

        if abs(tmp) < ans_diff:
            ans_diff = abs(tmp)
            ans_left = i
            ans_right = mid

            if tmp == 0:
                break
        if tmp >= 0:
            end = mid - 1
        else:
            start = mid + 1

print(lst[ans_left], lst[ans_right])
