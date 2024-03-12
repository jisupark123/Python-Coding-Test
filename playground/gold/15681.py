import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline


N, R, Q = map(int, input().split())

tree = [[] for _ in range(N + 1)]  # tree[n][0] -> n의 부모

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


dp = [0] * (N + 1)


# x의 서브트리 개수
def dfs(x):
    dp[x] = 1

    for nx in tree[x]:
        if dp[nx] == 0:
            dfs(nx)
            dp[x] += dp[nx]


dfs(R)

for _ in range(Q):
    query = int(input())
    print(dp[query])
