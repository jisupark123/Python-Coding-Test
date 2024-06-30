# 터렛

"""
두 점의 거리가 r1+r2보다 크면 0
두 점의 거리가 r1+r2과 같으면 1
두 점의 거리가 r1+r2보다 작으면 2
"""


def distance(x1, x2, y1, y2):
    return ((y1 - x1) ** 2 + (y2 - x2) ** 2) ** 0.5


for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d = distance(x1, x2, y1, y2)
    print(d)
    if d > r1 + r2:
        print(0)
    elif d == r1 + r2:
        print(1)
    else:
        print(2)
