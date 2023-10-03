import sys

input = sys.stdin.readline

n = int(input())

paper = [[0] * 100 for _ in range(100)]  # 100 x 100 종이
color_papers = [list(map(int, input().split())) for _ in range(n)]  # 색종이

for color_paper in color_papers:
    # 색종이가 시작하는 row -> 종이의 크기 - 종이의 아래변과의 거리 - 색종이의 크기(10)
    row = 100 - color_paper[1] - 10
    col = color_paper[0]  # 색종이가 시작하는 col

    # 색종이의 넓이만큼 칠하기
    for i in range(10):
        for j in range(10):
            paper[row + i][col + j] = 1


res = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            res += 1


print(res)
