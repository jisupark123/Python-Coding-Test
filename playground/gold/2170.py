# 선 긋기

"""
점의 위치가 -10억 ~ 10억이기 때문에 리스트에 직접 선을 그릴 수 없다.
따라서 스위핑 알고리즘을 적용한다.

- 좌표를 시작점 기준으로 정렬한다.
- Start, End 변수를 만든다.

경우 1 - 새로운 선을 그을 때 (x1이 End보다 클 때)
-> End-Start를 ans에 추가하고 새로운 좌표로 Start, End를 초기화한다.

경우 2 - 기존의 선과 겹칠 때 (x2가 End보다 클 때)
-> End를 x2로 확장한다.

경우 3 - 기존의 선과 아예 겹칠 때 (x2가 End보다 작거나 같을 때)
-> 아무것도 하지 않는다.
"""

import sys

input = sys.stdin.readline

N = int(input())


coordinates = [list(map(int, input().split())) for _ in range(N)]
coordinates.sort()

start, end = coordinates[0]
ans = 0

for x1, x2 in coordinates[1:]:

    if x1 > end:
        ans += end - start
        start, end = x1, x2

    if x2 > end:
        end = x2

ans += end - start

print(ans)
