# 선분 교차 2

"""
CCW 
- 평면 위에 놓여진 세 점(A,B,C)의 방향관계를 구할 수 있는 방법
- A-B 벡터와 A-C 벡터가 시작점을 공유하고 있을 때 A-B 벡터를 기준으로 A-C 벡터가 시계/반시계/일직선(평행) 방향으로 돌아가있는지 구할 수 있다.
- CCW는 A-B, A-C 두 벡터의 행렬식으로 구할 수 있으며, 
0보다 크면 A-C 벡터가 A-B 벡터를 기준으로 반시계(왼쪽) 방향으로 돌아가있는 것이고, 0보다 크면 시계방향, 0이면 일직선 상에 놓여져 있는 것이다.


선분 교차 판별 (한 선분의 끝 점이 다른 선분이나 끝 점 위에 있는 것도 교차하는 것이다)

두 선분(A-B, C-D)이 주어질 때, A-B와 C, A-B와 D, C-D와 A, C-D와 B, 총 4개의 CCW를 구할 수 있다.
이 때 A-B에 대한 CCW들을 곱했을 때 0이나 음수가 나오고, C-D에 대한 CCW들을 곱했을 때 역시 0이나 음수가 나오면 두 선분은 교차하는 것이다.

예외 사항 
- 두 선분이 일직선 상에 평행할 때 (모든 ccw가 0이 나온다)
- 이 경우에는 두 선분이 닿아 있는지 추가로 판별해야 한다. (닿아 있다면 교차)
"""


# 3점을 받아서 ccw를 계산
# b가 가운데 점
def ccw(a, b, c):
    return (a[0] - b[0]) * (b[1] - c[1]) - (a[1] - b[1]) * (b[0] - c[0])


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

A, B, C, D = [x1, y1], [x2, y2], [x3, y3], [x4, y4]

if ccw(A, B, C) * ccw(A, B, D) == 0 and ccw(C, D, A) * ccw(C, D, B) == 0:
    if (
        min(x1, x2) <= max(x3, x4)
        and min(x3, x4) <= max(x1, x2)
        and min(y1, y2) <= max(y3, y4)
        and min(y3, y4) <= max(y1, y2)
    ):
        print(1)
    else:
        print(0)

elif ccw(A, B, C) * ccw(A, B, D) <= 0 and ccw(C, D, A) * ccw(C, D, B) <= 0:
    print(1)
else:
    print(0)
