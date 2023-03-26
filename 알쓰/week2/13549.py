# 숨바꼭질 3

# N에서의 가장 빠른 시간 ->
# max(1~3번)
# 1. N + 1 에서의 가장 빠른 시간 + 1
# 2. N - 1 에서의 가장 빠른 시간 + 1
# 3. N * 2 에서의 가장 빠른 시간

# def dfs(n,sec):
#     if n == finish

from collections import deque

start, finish = map(int, input().split())

# -1 -> 방문을 한 번도 안함
# 0~ -> finish까지 걸리는 시간
dp = [-1] * (max(start, finish) * 3)
dp[start] = 0
dp[finish] = abs(start - finish)
queue = deque([start])
while queue:
    n = queue.popleft()
    if dp[n] >= dp[finish]:
        continue
    if n < finish:
        if dp[n * 2] == -1 or dp[n] < dp[n * 2]:
            dp[n * 2] = dp[n]
            queue.append(n * 2)
        if dp[n + 1] == -1 or dp[n] + 1 < dp[n + 1]:
            dp[n + 1] = dp[n] + 1
            queue.append(n + 1)
        if n != 0 and (dp[n - 1] == -1 or dp[n] + 1 < dp[n - 1]):
            dp[n - 1] = dp[n] + 1
            queue.append(n - 1)
    elif n > finish:
        if dp[n - 1] == -1 or dp[n] + 1 < dp[n - 1]:
            dp[n - 1] = dp[n] + 1
            queue.append(n - 1)

print(dp[finish])
