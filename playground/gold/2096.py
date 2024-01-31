# 내려가기

"""
a행에서 b번째로 내려갔을 때의 최댓값 -> f(a,b)
f(a,b) = max of f(a+1, 1) | f(a+1, 2) | f(a+1, 3)
"""


import sys

input = sys.stdin.readline


N = int(input())

mapping = [(0, 1), (0, 1, 2), (1, 2)]
arr = list(map(int, input().split()))
max_dp = arr[:]
min_dp = arr[:]

# 새로 들어오는 인풋 관점에서, 이전줄에서 어느 숫자가 내려오는게 좋을지 정한다.
for _ in range(N - 1):
    next_arr = list(map(int, input().split()))
    max_dp = [max([max_dp[x] + next_arr[a] for x in mapping[a]]) for a in range(3)]
    min_dp = [min([min_dp[x] + next_arr[a] for x in mapping[a]]) for a in range(3)]

print(max(max_dp), min(min_dp))
