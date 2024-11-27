# 디지털 트윈

"""
위로 올라가거나 왔던 곳을 다시 가는 것은 불가능
하나의 라인에서 시작점은 생산기계들의 왼쪽 끝 or 오른쪽 끝일 수밖에 없음
내려갈 때에도 다음 라인의 생산기계의 왼쪽 끝 or 오른쪽 끝으로 가야함
그러므로 하나의 라인에서 결정이 필요한 지점은 2곳

d -> 왼쪽/오른쪽
f(x, d) -> x 라인에서 생산 기계의 d(왼쪽/오른쪽) 끝에서부터 시작하여 반대쪽으로 이동할 때 최단 경로
d(l, r) -> x 라인의 왼쪽(l) 생산 기계부터 x+1 라인의 오른쪽(r) 생산 기계까지의 맨해튼 거리
s(x) -> x 라인의 맨왼쪽 생산 기계와 맨오른쪽 생산 기계의 거리

if d가 왼쪽이고 x 라인 다음에 생산 기계가 없는 라인이 존재한다면 f(x, d) = min(f(x+1, 왼쪽) + d(r, l) + s(x), f(x+1, 오른쪽) + d(r, r))
if d가 오른쪽이고 x 라인 다음에 생산 기계가 없는 라인이 존재한다면 f(x, d) = min(f(x+1, 왼쪽) + d(l, l) + s(x), f(x+1, 오른쪽) + d(l, r))

if d가 왼쪽이고 x+1 라인의 생산 기계의 왼쪽 끝이 x의 오른쪽 끝보다 왼쪽이라면 f(x, d) = f(x+1, 오른쪽) + d(r, r) + s(x)
if d가 왼쪽이고 x+1 라인의 생산 기계의 왼쪽 끝이 x의 오른쪽 끝과 같거나 오른쪽이라면 f(x, d) = min(f(x+1, 왼쪽) + d(r, l) + s(x), f(x+1, 오른쪽) + d(r, r) + s(x))

if d가 오른쪽이고 x+1 라인의 생산 기계의 오른쪽 끝이 x의 왼쪽 끝보다 오른쪽이라면 f(x, d) = f(x+1, 왼쪽) + d(l, l) + s(x)
if d가 오른쪽이고 x+1 라인의 생산 기계의 오른쪽 끝이 x의 왼쪽 끝과 같거나 왼쪽이라면 f(x, d) = min(f(x+1, 왼쪽) + d(l, l) + s(x), f(x+1, 오른쪽) + d(l, r) + s(x))


coord_dict 
-> [X x 3 배열]

-> 인덱스 0과 1에는 하나의 라인에서 생산 기계의 왼쪽 끝과 오른쪽 끝의 인덱스를 저장 
-> ex. coord_dict[1][0] -> 1번째 라인의 맨 왼쪽 생산 기계의 인덱스

-> 인덱스 2에는 해당 라인 아래에 생산 기계가 없는 라인이 있는지 여부 저장 (0/1)
-> ex. coord_dict[1][2]가 1이라면 1번째 라인 아래에 생산 기계가 없는 라인이 존재, 0이면 존재 X

-> 0번째 라인에 생산 기계가 없다면 시작점(0)으로 지정
-> 마지막 라인에 생산 기계가 없다면 도착점(N-1)으로 지정
-> 생산 기계가 없는 라인은 저장 x
-> n번째 라인에 생산 기계가 하나라면 두 값은 동일
"""

import sys

input = sys.stdin.readline


# item의 왼쪽에서 첫번째 인덱스, 오른쪽에서 첫번째 인덱스를 return
def index(lst, item):
    try:
        a = lst.index(item)
    except:
        a = None

    try:
        b = N - lst[::-1].index(item) - 1
    except:
        b = None

    return a, b


# x 라인의 a에서 x+1 라인의 b까지의 맨해튼 거리
def distance(a, b):
    return abs(a - b) + 1


N = int(input())
factory = [list(map(int, list(input().strip()))) for _ in range(N)]

# coord_dict[x][0] -> x 라인의 왼쪽 끝 생산 기계의 열 인덱스
# x 라인에 생산 기계가 없다면 x+1 라인과 동일하게 적용
# N-1번째 라인에 생산 기계가 없다면 N-1(도착점)으로 적용
coord_dict = []
empty_line_cnt = 0

# 첫번째 라인에 생산 기계가 없다면 시작점으로 지정

l, r = index(factory[0], 1)
if l is None and r is None:
    coord_dict.append([0, 0, 0])
else:
    coord_dict.append([l, r, 0])

for line in factory[1:-1]:
    l, r = index(line, 1)
    if l is None and r is None:
        empty_line_cnt += 1
        if coord_dict:
            coord_dict[-1][2] = 1
    else:
        coord_dict.append([l, r, 0])


# 마지막 라인에 생산 기계가 없다면 도착점으로 지정
l, r = index(factory[-1], 1)
if l is None and r is None:
    coord_dict.append([N - 1, N - 1, 0])
else:
    coord_dict.append([l, r, 0])


# dp[x][0] -> x 라인에서 생산 기계의 왼쪽 끝에서부터 시작하여 오른쪽으로 이동할 때의 최단 경로
# dp[x][1] -> x 라인에서 생산 기계의 오른쪽 끝에서부터 시작하여 왼쪽으로 이동할 때의 최단 경로
dp = [[float("inf")] * 2 for _ in range(len(coord_dict))]

dp[-1][0] = N - 1 - coord_dict[-1][0]


for x in range(len(dp) - 2, -1, -1):
    x_left, x_right, _ = coord_dict[x]
    nx_left, nx_right, _ = coord_dict[x + 1]
    space = x_right - x_left

    if coord_dict[x][2] == 1:
        dp[x][0] = min(
            dp[x + 1][0] + distance(x_right, nx_left) + space,
            dp[x + 1][1] + distance(x_right, nx_right) + space,
        )
        dp[x][1] = min(
            dp[x + 1][0] + distance(x_left, nx_left) + space,
            dp[x + 1][1] + distance(x_left, nx_right) + space,
        )
        continue

    if nx_left < x_right:
        dp[x][0] = dp[x + 1][1] + distance(x_right, nx_right) + space
    else:
        dp[x][0] = min(
            dp[x + 1][0] + distance(x_right, nx_left) + space,
            dp[x + 1][1] + distance(x_right, nx_right) + space,
        )

    if nx_right > x_left:
        dp[x][1] = dp[x + 1][0] + distance(x_left, nx_left) + space
    else:
        dp[x][1] = min(
            dp[x + 1][0] + distance(x_left, nx_left) + space,
            dp[x + 1][1] + distance(x_left, nx_right) + space,
        )

default_space = coord_dict[0][0] + 1
ans = default_space + empty_line_cnt + dp[0][0]
print(-1 if ans == float("inf") else ans)
