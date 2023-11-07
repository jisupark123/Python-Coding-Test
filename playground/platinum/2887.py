# 행성 터널
"""
최소 스패닝 트리 알고리즘

Prim 알고리즘을 사용

프림 알고리즘 -> 
다익스트라와 거의 똑같다. 
다만 출발지로부터의 가중치 리스트를 업데이트하는 다익스트라와 다르게 프림은 우선순위가 높은 가중치의 합을 구한다.

이 문제는 모든 노드가 서로 연결되어 있는 그래프이다.
따라서 그래프를 만들어놓지 않고 그때그때 가중치를 계산하는 방식을 사용한다.

프림 알고리즘은 시간/메모리초과 -> 모든 간선을 계산하고 큐에 넣는 점이 문제다.

-------------------------------------------------------------

Kruscal 알고리즘을 사용

Kruscal 알고리즘 ->
처음에 모든 노드는 각각 하나의 집합으로 시작한다.
이후 비용이 최소인 간선을 차례로 택하면서 집합을 합쳐나간다.
최종적으로 모든 노드(집합)가 하나의 집합으로 합쳐지면 종료.

Kruscal 알고리즘을 구현하기 위해선 edge들을 정렬해야 한다.
하지만 N이 최대 10만개이고 각 노드가 서로 연결되어 있는 이 문제에선 모든 간선을 정렬할 수 없다.

간선의 크기는 다음과 같이 구할 수 있다. min(|xA-xB|, |yA-yB|, |zA-zB|) 
x,y,z 각각의 좌표들을 묶어서 정렬하면 각각의 축(x,y,z)에서 각 아이템의 인접한 두개의 노드를 찾을 수 있다. (i, i+1)
이렇게 간선의 크기를 각각의 축에서 계산하고 이들을 최소 힙에 넣으면 O(N) * 3 시간 내에 알고리즘을 구현할 수 있다.
"""

import sys


# x node가 속한 집합의 대표 노드를 return
def find(x: int) -> int:
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])  # 크루스칼 알고리즘에서 한번 생성된 집합은 바뀌지 않기 때문에 부모를 대표 노드로 최적화한다.
    return parents[x]


# x node와 y node가 속한 집합을 union
def union(x: int, y: int) -> None:
    parents[find(x)] = find(y)


input = sys.stdin.readline

N = int(input())
planets = [[*list(map(int, input().split())), i] for i in range(N)]


edges = []
for i in range(3):
    planets.sort(key=lambda x: x[i])  # x,y,z를 기준으로 정렬
    for j in range(N - 1):
        edges.append(
            (abs(planets[j][i] - planets[j + 1][i]), planets[j][3], planets[j + 1][3])
        )

edges.sort()
parents = [x for x in range(N)]
ans = 0

for cost, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        ans += cost

print(ans)


# import sys
# import heapq

# input = sys.stdin.readline

# N = int(input())
# coordinates = [list(map(int, input().split())) for _ in range(N)]

# ans = 0
# queue = [(0, 0)]
# visited = [0 for _ in range(N)]
# loop_cnt = 0

# while queue:
#     cost, node = heapq.heappop(queue)
#     if visited[node]:
#         continue
#     visited[node] = 1
#     ans += cost
#     x1, y1, z1 = coordinates[node]
#     for next_node in range(N):
#         if node != next_node and not visited[next_node]:
#             x2, y2, z2 = coordinates[next_node]
#             next_cost = min(abs(x1 - x2), abs(y1 - y2), abs(z1 - z2))
#             heapq.heappush(queue, (next_cost, next_node))

# print(ans)
