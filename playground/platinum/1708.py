# 볼록 껍질

"""
그레이엄 스캔 알고리즘

1. y가 가장 작은 점을 기준점으로 선택(같다면 x 좌표가 가장 낮은 점)
2. 기준점을 기준으로 모든 점을 각도 순으로 정렬 
3. 정렬된 점에 대해 순서대로 다음을 수행
3-1. 만약 스택의 마지막 두 점과 새로 추가되는 점이 ccw(반시계 방향)이면 push
3-2. ccw가 아니라면, ccw가 될 때까지 마지막 원소를 pop
4. 마지막으로 스택에 남아있는 점들이 볼록 껍질을 구성하는 점들이다.

"""

import sys
import math

input = sys.stdin.readline


# 기준점(p0)으로부터 p와의 각도를 계산하기 위한 함수
def polar_angle(p0, p):
    return math.atan2(p[1] - p0[1], p[0] - p0[0])


# 1이면 반시계 방향 | 0이면 일직선 | -1이면 시계 방향
def ccw(a, b, c):
    det = (a[0] - b[0]) * (b[1] - c[1]) - (a[1] - b[1]) * (b[0] - c[0])
    if det > 0:
        return 1
    if det < 0:
        return -1
    return 0


N = int(input())

points = [list(map(int, input().split())) for _ in range(N)]

# y 좌표가 가장 낮은 점(같다면 x 좌표가 가장 낮은 점)을 찾음
p0 = min(points, key=lambda p: (p[1], p[0]))

# p0을 기준으로 반시계 방향으로 정렬
points.sort(key=lambda p: (polar_angle(p0, p), p[1], p[0]))

# 스택 초기화
stack = [p0]

# 기준점과 마지막 2점이 일직선이 되는 것을 방지하기 위해 기준점을 한번 더 push
for p in points[1:] + [p0]:
    while len(stack) > 1 and ccw(stack[-2], stack[-1], p) <= 0:
        stack.pop()
    stack.append(p)


print(len(stack) - 1)  # 마지막으로 push한 기준점을 제외
