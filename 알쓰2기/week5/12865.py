# 평범한 배낭

"""
{w[0], w[1]...w[i]} -> i번째 까지의 물건들의 Set = S(i)
w[i]의 가치 -> v[i]
K 무게를 담을 수 있을 때 가치 V의 최댓값 -> V(S(i), K)
V(S(i), K) = max of V(Set(i-1), K - w[i]) + v[i], V(Set(i-1), K)

각각의 V(K, S(W))을 저장하자
i -> 행
k -> 열
V(S(i), k) -> 원소

i행 k열 -> 물건이 i번째까지있고 가방의 용량이 k개 있을 때 담을 수 있는 가치의 최댓값

"""

import sys

input = sys.stdin.readline

N, K = map(int, input().split())

items = [[0, 0]]  # 무게, 가치
for _ in range(N):
    items.append(list(map(int, input().split())))

# dp[i][j] -> 물건의 종류가 ~i까지 있고 가방의 용량이 j개 있을 때 담을 수 있는 가치의 최댓값
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):  # 무게
    for j in range(1, K + 1):  # 가치
        w = items[i][0]
        v = items[i][1]

        if j < w:  # 물건의 용량이 최대 적재 용량을 초과한다면 뽑을 가능성 X, 따라서 set에서 제외시킨다.
            dp[i][j] = dp[i - 1][j]
        else:  # 물건을 뽑거나 뽑지 않거나
            dp[i][j] = max(dp[i - 1][j - w] + v, dp[i - 1][j])

print(dp[N][K])
