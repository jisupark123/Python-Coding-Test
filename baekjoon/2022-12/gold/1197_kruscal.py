# 최소 스패닝 트리(최소 신장 트리)
# 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리
# 크루스칼 알고리즘을 사용
from sys import stdin

input = stdin.readline


V, E = map(int, input().split())
parent = [x for x in range(V + 1)]  # 모든 노드는 크기가 1인 집합으로 시작한다.
edges = []
res = 0
for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append([a, b, c])  # a에서 b로 가는데 드는 비용 c
edges.sort(key=lambda x: x[2])  # 가중치가 적은 간선순으로 정렬


def find(x: int) -> int:  # 부모 찾기
    if parent[x] == x:  # 인덱스와 값이 일치하면 대표 노드
        return x
    parent[x] = find(parent[x])  # 크루스칼 알고리즘에서 한번 생성된 집합은 바뀌지 않기 때문에 부모를 대표 노드로 최적화한다.
    return parent[x]


# 원래 union 연산에는 가지가 깊은 트리(집합)가 부모가 되지만
# 어차피 find 연산에서 트리의 높이를 1로 최적화하기 때문에 생략한다.
def union(x: int, y: int) -> None:
    parent[find(x)] = find(y)


for a, b, cost in edges:
    if find(a) != find(b):  # 같은 집합에 속해있지 않다면 간선을 택하고 집합을 병합한다.
        union(a, b)
        res += cost

print(res)
