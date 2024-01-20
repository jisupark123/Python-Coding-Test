# 숨바꼭질 2

"""
f(x) -> x에서 목적지로 가는 최소 시간
f(x) = min of f(x*2) + 1, f(x+1) + 1, f(x-1)
"""

import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

limit = 100000 * 2
res = 0  # 가장 빠른 시간으로 찾는 방법이 몇 가지 인지
min_time = float("inf")

queue = deque()  # (시간, 위치)
queue.append((0, N))

dp = [float("inf")] * limit  # dp[n] = n에서 K까지 걸리는 최소 시간

while queue:
    time, x = queue.popleft()

    if time > min_time:
        break
    if x == K:
        min_time = time
        res += 1
        continue

    for nx in (x - 1, x + 1, x * 2):
        if 0 <= nx < limit and dp[nx] >= time + 1:
            dp[nx] = time + 1
            queue.append((time + 1, nx))


print(min_time)
print(res)
