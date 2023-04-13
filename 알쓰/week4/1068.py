# 트리

import sys

input = sys.stdin.readline

N = int(input())


# 부모 -> 자식
graph = [[] for _ in range(N)]  # graph[i] -> i 번째 노드의 자식 노드들 번호 리스트
parents = list(map(int, input().split()))  # 부모 노드
root_node = 0  # 루트 노드
delete_node = int(input())  # 삭제할 노드


for i in range(N):
    if parents[i] == -1:  # 부모 노드가 -1이면 루트 노드
        root_node = i
    else:
        # 삭제할 노드가 아닌 경우만 부모의 자식 리스트에 추가
        if i != delete_node:
            graph[parents[i]].append(i)

if delete_node == root_node:
    print(0)
    exit(0)


res = 0


def dfs(node: int):
    global res

    # 자식이 없으면 리프노드
    if len(graph[node]) == 0:
        res += 1
        return
    for n in graph[node]:
        dfs(n)


dfs(root_node)

print(res)
