# 색종이 만들기

import sys

input = sys.stdin.readline


def check(paper):
    global white, blue
    color = paper[0][0]
    for i in paper:
        for j in i:
            if j != color:
                return False
    if color == 0:
        white += 1
    else:
        blue += 1
    return True


def slice_paper(paper):
    if check(paper) == True:
        return

    else:
        n = len(paper)
        slice_paper([x[0 : n // 2] for x in paper[0 : n // 2]])
        slice_paper([x[n // 2 :] for x in paper[0 : n // 2]])
        slice_paper([x[0 : n // 2] for x in paper[n // 2 :]])
        slice_paper([x[n // 2 :] for x in paper[n // 2 :]])


N = int(input())
color_paper = [list(map(int, input().split())) for _ in range(N)]

white = 0  # 0
blue = 0  # 1

slice_paper(color_paper)

print(white)
print(blue)
