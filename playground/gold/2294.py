# 동전 2

"""
dp + 이분 탐색

N - 동전의 개수
v[i] i번째 동전의 가치
f(n, k)
-> n개의 동전으로 k를 만들 수 있나
-> f(n-1, k-v[i]) or f(n-1, k-v[i+1]) or ... f(n-1, k-v[N])
"""

"""
N - 동전의 개수
v[i] i번째 동전의 가치
f(k)
-> 가진 동전들로 k원을 만들었을 때 최소가 되는 동전의 개수
-> min(f(k-v[i]), i -> 0 ~ N) + 1
"""

import sys

input = sys.stdin.readline
N, K = map(int, input().split())

v = [int(input()) for _ in range(N)]


dp = [0] * (K + 1)


for i in range(N):
    if v[i] < K + 1:
        dp[v[i]] = 1

for k in range(K + 1):
    for i in range(N):
        if k - v[i] >= 0 and dp[k - v[i]] != 0:
            if dp[k] == 0:
                dp[k] = dp[k - v[i]] + 1
            else:
                dp[k] = min(dp[k], dp[k - v[i]] + 1)

if dp[K] == 0:
    print(-1)
else:
    print(dp[K])
