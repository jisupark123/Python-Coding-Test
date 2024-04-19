# 전깃줄

"""
1. A 블럭에서 숫자가 낮은 순으로 전깃줄을 정렬한다.
2. 정렬된 전깃줄을 순서대로 하나씩 선택한다고 했을 때, 다음에 올 전깃줄은 이전보다 큰 B를 가져야 한다.
3. 순서대로 하나씩 전깃줄을 선택할 때, 교차하지 않고 최대한 많은 전깃줄을 선택하는 방법을 찾아야 함

가장 긴 증가하는 부분 수열(LIS) 문제로 변환 가능


DP 알고리즘

f(n)
-> n을 선택했을 때, n부터 가장 긴 증가하는 부분 수열
-> 1 + max of |오른쪽에서 n보다 큰 수들(n^)의 f(n^)|
"""

import sys

input = sys.stdin.readline


N = int(input())

lines = sorted([list(map(lambda x: int(x) - 1, input().split())) for _ in range(N)])

is_cross = [[0] * (N) for _ in range(N)]  # 서로 교차하는지 미리 계산

for i in range(N):
    for j in range(N):
        if i != j:
            if (lines[i][0] - lines[j][0]) * (lines[i][1] - lines[j][1]) < 0:
                is_cross[i][j] = 1


dp = [1] * N  # dp[n] -> n을 선택했을 때, n부터 시작된 lis의 최대 길이

for i in range(N - 1, -1, -1):
    for j in range(i + 1, N):
        if lines[i][1] < lines[j][1]:
            dp[i] = max(dp[i], 1 + dp[j])

print(N - max(dp))
