# 뱀과 사다리 게임

# n -> n번째 칸에 도착하기 위해 주사위를 굴려야 하는 횟수의 최솟값

# 뱀이고 b가 0이면 -> b = a -> queue.append(b)
# 사다리고 b가 0이면 -> b = a -> queue.append(b)

# 뱀이고 a > b면 -> continue
# 사다리고 a > b면 -> continue

# 뱀이고 b > a면 -> b = a -> queue.append(b)
# 사다리고 b > a면 -> b = a -> queue.append(b)

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

ledders = [tuple(map(int, input().split())) for _ in range(N)]
snakes = [tuple(map(int, input().split())) for _ in range(M)]

info = [0] * 101

# 0 -> 한 번도 방문하지 않음
# 1~ -> 시작점에서의 최솟값
dp = [0] * 101

for a, b in ledders:
    info[a] = b
for a, b in snakes:
    info[a] = b

queue = deque([1])

while queue:
    n = queue.popleft()
    if n == 100:
        continue
    if info[n] != 0:
        if dp[info[n]] == 0 or dp[info[n]] > dp[n]:
            dp[info[n]] = dp[n]
            queue.append(info[n])
        continue
    for i in range(1, 7):
        if n + i <= 100 and (dp[n + i] == 0 or dp[n + i] > dp[n] + 1):
            dp[n + i] = dp[n] + 1
            queue.append(n + i)

print(dp[100])

for i in range(1, 100, 10):
    try:
        print(dp[i : i + 10])
    except:
        print(dp[i:])
