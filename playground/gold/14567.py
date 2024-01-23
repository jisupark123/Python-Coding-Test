# 선수과목 (Prerequisite)

import sys

input = sys.stdin.readline

N, M = map(int, input().split())


graph = [[] for _ in range(N + 1)]  # graph[n] -> 선수과목이 n인 과목들

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

dp = [0] * (N + 1)

# 각 숫자마다 인접한 노드 순회
# 현재 숫자 + 1, 인접한 노드 중 큰 값으로 업데이트
for i in range(1, N + 1):
    for x in graph[i]:
        dp[x] = max(dp[x], dp[i] + 1)

print(" ".join(map(lambda x: str(x + 1), dp[1:])))
