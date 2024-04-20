# 앱

"""
i번째 앱까지 중 j코스트로 얻을 수 있는 최대의 byte (배낭 문제)

- A1 ~ Ai까지 앱 중에, j코스트로 얻을 수 있는 최대의 byte -> f(i, j)
- f(i, j) = max of f(i-1, j-cost[i]) + memory[i] | f(i-1, j)
- i번째 앱을 비활성화 하거나 하지 않거나

M 바이트 이상을 확보한 것 중 가장 cost가 적은 value가 정답


- 하향식으로 해결할 경우, 모든 코스트(j)에 대해 탐색하기 위해 for문을 직접 돌려주어야 한다.
- 상향식으로 해결할 경우, 내부 for문에 의해 자동으로 모든 코스트(j)에 대해 탐색된다.

이 문제의 경우, 모든 cost에 대해 dp 배열을 채워야 하므로 상향식으로 푸는 것이 유리하다.
"""


N, M = map(int, input().split())

memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

############ 하향식 풀이 ###############

# dp = [[-1] * (sum(cost) + 1) for _ in range(N + 1)]


# def dfs(i, j):
#     if i < 0:  # 앱이 0개라면 얻을 수 있는 최대의 byte도 0
#         return 0

#     if dp[i][j] != -1:
#         return dp[i][j]

#     if cost[i] <= j:  # 비활성화 하려는 앱의 비용이 j를 초과하는지 검사
#         dp[i][j] = max(dfs(i - 1, j - cost[i]) + memory[i], dfs(i - 1, j))
#     else:  # 초과한다면 앱 i는 놔둠
#         dp[i][j] = dfs(i - 1, j)

#     return dp[i][j]


# # 적은 코스트부터 하나씩 test
# for c in range(sum(cost) + 1):
#     if dfs(N - 1, c) >= M:
#         print(c)
#         break


############ 상향식 풀이 ###############

dp = [[0] * (sum(cost) + 1) for _ in range(N + 1)]

for i in range(N):
    for j in range(sum(cost) + 1):
        if cost[i] <= j:  # 비활성화 하려는 앱의 비용이 j를 초과하는지 검사
            dp[i][j] = max(dp[i - 1][j - cost[i]] + memory[i], dp[i - 1][j])
        else:  # 초과한다면 앱 i는 놔둠
            dp[i][j] = dp[i - 1][j]

for c, m in enumerate(dp[N - 1]):
    if m >= M:
        print(c)
        break
