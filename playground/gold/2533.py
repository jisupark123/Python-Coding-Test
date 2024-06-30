# 사회망 서비스(SNS)

"""
dp = N * 2 크기의 2차원 배열
dp[x][0] - x가 루트 노드이고 x가 얼리 어답터일 때, 서브 트리의 최대 얼리 어답터 수 (root 포함)
dp[x][1] - x가 루트 노드이고 x가 얼리 어답터가 아닐 때, 서브 트리의 최대 얼리 어답터 수

x의 자식이 없을 때
- dp[x][0] = 1
- dp[x][1] = 0

x의 자식이 있을 때
nx - x의 자식(들)
- dp[x][0] = 1 + sum(max(dp[nx][0], dp[nx][1])) (자식들에 대해 모두 더하기)
- dp[x][1] = sum(dp[nx][0])
"""

import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

N = int(input())

tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dp = [[-1] * 2 for _ in range(N + 1)]


# p = 부모
def dfs(p, x):
    if len(tree[x]) == 1 and tree[x][0] == p:
        dp[x][0] = 1
        dp[x][1] = 0
        return

    for nx in tree[x]:
        if nx != p:
            dfs(x, nx)

    dp[x][0] = 1 + sum((min(dp[nx][0], dp[nx][1]) for nx in tree[x] if nx != p))
    dp[x][1] = sum((dp[nx][0] for nx in tree[x] if nx != p))


dfs(-1, 1)
print(min(*dp[1]))
