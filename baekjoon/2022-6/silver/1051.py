# 숫자 정사각형

import sys


def get_max_area(h, w):
    res = 1
    for i in range(1, min(height - h, width - w)):
        if (
            rectangle[h][w]
            == rectangle[h + i][w]
            == rectangle[h][w + i]
            == rectangle[h + i][w + i]
        ):
            res = max((i + 1) ** 2, res)
    return res


input = sys.stdin.readline
height, width = map(int, input().rstrip().split())

rectangle = [list(map(int, list(input().rstrip()))) for _ in range(height)]

max_area = 1

for h in range(height - 1):
    for w in range(width - 1):
        new_area = get_max_area(h, w)
        max_area = max(new_area, max_area)

print(max_area)
