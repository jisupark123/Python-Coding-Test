# 개구리 점프

"""
- a 통나무에서 b 통나무로 이동할 수 있는지 -> a의 시작점 <= b의 시작점 <= a의 끝점
- 이동할 수 있는 통나무들을 같은 집합으로 합치기 -> union-find 사용
- 원래는 bfs나 dfs로 해결할 수 있지만 시작점을 기준으로 정렬하면 통나무마다 한 번씩만 union-find 연산을 수행하면 된다. 
단, 끝점을 최댓값으로 업데이트 해야됨
(O(n) * union-find)
"""

import sys

input = sys.stdin.readline


def find(x):
    if x == parent[x]:
        return x

    # 경로 압축
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    parent[find(a)] = find(b)


N, Q = map(int, input().split())

woods = []
for i in range(N):
    x1, x2, _ = map(int, input().split())
    woods.append([x1, x2, i])
woods.sort()

parent = [x for x in range(N)]

end = -sys.maxsize

for i in range(N - 1):
    end = max(end, woods[i][1])
    if woods[i + 1][0] <= end:
        union(woods[i][2], woods[i + 1][2])


for _ in range(Q):
    a, b = map(lambda x: int(x) - 1, input().split())
    print(1 if find(a) == find(b) else 0)
