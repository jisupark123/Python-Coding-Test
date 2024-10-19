# 직각다각형

"""
w -> 가로 선분을 저장할 리스트
h -> 세로 선분을 저장할 리스트

1. 들어온 꼭짓점과 이전의 점을 비교하여 가로/세로선을 판별
1-1. 가로선이면 w에, 세로선이면 h에 push.
1-2. 이때 크기가 작으면 [점, 1], 크면 [점, -1] 형태로 push

2. w, h를 점의 크기를 오름차순하여 정렬.
3. 가로, 세로 선분 각각 imos 누적합 알고리즘으로 겹친 선분의 개수를 count
"""

import sys

input = sys.stdin.readline


n = int(input())

h = []  # 세로선
w = []  # 가로선

sx, sy = map(int, input().split())
px, py = sx, sy

for i in range(n):

    if i != n - 1:
        x, y = map(int, input().split())
    else:  # 처음 들어온 점을 마지막에 넣어줌
        x, y = sx, sy

    if px == x:  # y만 바뀌면 세로선
        points = sorted([[py, 1], [y, 1]])
        points[1] = [points[1][0], -1]
        h.extend(points)
    else:
        points = sorted([[px, 1], [x, 1]])
        points[1] = [points[1][0], -1]
        w.extend(points)

    px = x
    py = y

# 점의 크기를 오름차순하여 정렬하고, 같으면 선분의 끝점(1 or -1)을 오름차순하여 정렬
h.sort()
w.sort()


# imos 누적합
def max_overlap(lines):
    res = 0
    line_cnt = 0

    for line in lines:
        line_cnt += line[1]
        res = max(res, line_cnt)

    return res


print(max(max_overlap(h), max_overlap(w)))
