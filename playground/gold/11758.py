# CCW

"""
ccw가 음수면 반시계 방향, 0이면 일직선상 평행, 양수면 시계 방향
"""


# 3점을 받아서 ccw를 계산
# b가 가운데 점
def ccw(a, b, c):
    return (a[0] - b[0]) * (b[1] - c[1]) - (a[1] - b[1]) * (b[0] - c[0])


a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

res = ccw(a, b, c)

if res < 0:
    print(-1)
elif res == 0:
    print(0)
else:
    print(1)
