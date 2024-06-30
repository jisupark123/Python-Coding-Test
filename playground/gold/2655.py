# 가장높은탑쌓기

"""
1. 벽돌의 넓이를 기준으로 정렬(내림차순)
2. 벽돌의 무게를 내림차순으로 유지하면서 높이의 합을 최대로 하는 시퀀스 찾기

bricks - 넓이를 기준으로 내림차순 정렬된 벽돌
S - 벽돌의 무게를 내림차순으로 유지하면서 높이의 합을 최대로 하는 시퀀스

f(n) - n번째 벽돌이 시작점인 S의 높이 합
f(n) = bricks[n] + max(bricks[n]보다 무게가 적게 나가는 벽돌들(n^)의 f(n^))

완성된 dp 배열에서 최댓값인 인덱스(argmax)를 뽑은 뒤 차이가 breaks[i]만큼 나는 벽돌을 추출한다.
"""

import sys

input = sys.stdin.readline

N = int(input())

# 원래 index를 추가해서 넣어줌
bricks = [list(map(int, input().split())) + [x + 1] for x in range(N)]
bricks.sort(reverse=True)

dp = [bricks[x][1] for x in range(N)]

for i in range(N - 1, -1, -1):
    for j in range(i + 1, N):
        if bricks[i][2] > bricks[j][2]:
            dp[i] = max(dp[i], bricks[i][1] + dp[j])

# argmax(dp)
max_i = 0
max_v = dp[0]

for i in range(1, N):
    if dp[i] > max_v:
        max_i = i
        max_v = dp[i]

ans = [bricks[max_i][3]]
v = max_v - bricks[max_i][1]


# dp 배열에서 차이가 높이만큼 나는 벽돌을 순서대로 추출
for i in range(max_i + 1, N):
    if dp[i] == v:
        ans.append(bricks[i][3])
        v -= bricks[i][1]

print(len(ans))
for x in ans[::-1]:
    print(x)
