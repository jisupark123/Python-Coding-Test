# 터렛

"""
두 원의 중심과 반지름을 입력했을 때, 두 원 사이의 접점의 개수를 구하는 문제

- 반지름 -> r1, r2
- 원의 중심 사이의 거리 -> d (두 점 사이의 거리 공식 사용)

1. 만나지 않는 경우 (접점이 0개)

1) 원이 다른 원을 포함하지 않을 때 (r1 + r2 < d)
2) 원이 다른 원을 포함할 때 (r1 - r2 > d)


2. 접하는 경우 (접점이 1개)

1) 외접 (r1 + r2 = d)
2) 내접 (r1 - r2 = d)


3. 두 점에서 만나는 경우 (접점이 2개)

1) r1 - r2 < d < r1 + r2


4. 두 원이 겹치는 경우 (접점이 무한대)

1) d = 0 and r1 = r2
"""


def distance(x1, x2, y1, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d = distance(x1, x2, y1, y2)

    if d == 0 and r1 == r2:
        print(-1)
    elif r1 + r2 == d or abs(r1 - r2) == d:
        print(1)
    elif abs(r1 - r2) < d < r1 + r2:
        print(2)
    else:
        print(0)
