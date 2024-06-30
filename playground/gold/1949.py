# 우수 마을

"""
dp = N * 2 * 2 크기의 2차원 배열
최적해 = '우수 마을'의 주민 수의 총 합 (모든 조건을 만족했을 때)

x가 루트 노드일 때
dp[x][0][0] = -1 (불가능)
dp[x][0][1] = x의 부모가 우수 마을이고 x가 우수 마을이 아닐 때, 서브 트리의 최적해
dp[x][1][0] = x의 부모가 우수 마을이 아니고 x가 우수 마을일 때, 서브 트리의 최적해
dp[x][1][1] = x의 부모가 우수 마을이 아니고 x도 우수 마을이 아닐 때, 서브 트리의 최적해

x의 자식이 없을 때
- dp[x][0][0] = -1 (불가능)
- dp[x][0][1] = 0
- dp[x][1][0] = x의 주민 수
- dp[x][1][1] = -1 (불가능)

x의 자식이 있을 때
nx - x의 자식(들)
- dp[x][0][0] = -1 (불가능)
- dp[x][0][1] = sum(max(dp[nx][1][0], dp[nx][1][1])) (자식들에 대해 모두 더하기)
- dp[x][1][0] = x의 주민 수 + sum(dp[nx][0][1])
- dp[x][1][1] = sum(dp[nx][1][0]) (자식들 중 하나만 우수마을이어도 됨)
"""

import sys

sys.setrecursionlimit(10**9)

input = sys.stdin.readline

N = int(input())

people = [0] + list(map(int, input().split()))

tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dp = [[[-1] * 2 for _ in range(2)] for _ in range(N + 1)]


# p_node = 부모 번호
# p_type = 부모가 우수 마을이면 0, 아니면 1
def dfs(p_node, x):
    if len(tree[x]) == 1 and tree[x][0] == p_node:
        dp[x][0][1] = 0
        dp[x][1][0] = people[x]
        return

    for nx in tree[x]:
        if nx != p_node:
            dfs(x, nx)

    dp[x][0][1] = sum(
        (max(dp[nx][1][0], dp[nx][1][1]) for nx in tree[x] if nx != p_node)
    )
    dp[x][1][0] = people[x] + sum((dp[nx][0][1] for nx in tree[x] if nx != p_node))
    dp[x][1][1] = max(
        (
            dp[i][1][0]
            + sum(
                (max(dp[j][1][0], dp[j][1][1]) for j in tree[x] if j not in (p_node, i))
            )
            for i in tree[x]
            if i != p_node
        )
    )


dfs(-1, 1)

print(max(*dp[1][1]))
