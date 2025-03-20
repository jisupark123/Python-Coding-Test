"""
f(x) = x가 루트일 때 모든 직원이 소식을 듣는데 걸리는 시간의 최솟값

상향식 DP로 각 노드마다 f(x)를 구함

x가 리프노드일 때 
-> f(x) = 0

x가 리프노드가 아닐 때 
-> list(x1, x2, ..., xn) = x의 자식 노드(x1, x2, ..., xn)를 f(x1, x2, ..., xn) 순으로 정렬한 배열 (큰 순서)
-> arr(x1, x2, ..., xn) = list(x1, x2, ..., xn) 각 원소에 1,2,...,n을 더한 배열
-> f(x) = max(arr(x1, x2, ..., xn))
(f(x)가 가장 큰 자식부터 탐색)
"""

import sys

input = sys.stdin.readline

N = int(input())

tree = [[] for _ in range(N)]

for i, parent in enumerate(map(int, input().strip().split())):
    if i != 0:
        tree[parent].append(i)

dp = [-1] * N


def dfs(x):
    if len(tree[x]) == 0:
        dp[x] = 0
        return

    for nx in tree[x]:
        dfs(nx)

    sorted_children = sorted(map(lambda x: dp[x], tree[x]), reverse=True)
    times = [i + c for i, c in enumerate(sorted_children, 1)]

    dp[x] = max(times)


dfs(0)

print(dp[0])
