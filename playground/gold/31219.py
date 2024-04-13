# 세계 일주

"""
여행 중 지나간 선분(시작점, 도착점)을 리스트에 저장해놓고, 새로운 경로를 탐험할 때 이미 지나갔던 선분과 교차하는지 검사한다.
"""

import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline


# 선분 a,b가 교차하는지 판정하는 함수
# 선분 a -> [[시작점x, 시작점y], [도착점x, 도착점y]]
def is_cross(a, b):

    # a-b, b-c
    def ccw(a, b, c):
        return (a[0] - b[0]) * (b[1] - c[1]) - (a[1] - b[1]) * (b[0] - c[0])

    A, B, C, D = a[0], a[1], b[0], b[1]

    if ccw(A, B, C) * ccw(A, B, D) < 0 and ccw(C, D, A) * ccw(C, D, B) < 0:
        return True
    else:
        return False


def distance(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


def dfs(curr):

    # 모든 곳에 방문했다면
    if len(visited) == N:
        return distance(pos[curr], pos[start])

    min_cost = float("inf")
    for x in range(N):

        if x in visited:
            continue

        # 방문하지 않은 pos인지 검사
        flag = True
        for p in visited_path:
            if is_cross(p, [pos[curr], pos[x]]):
                # print(p, [pos[curr], pos[x]])
                flag = False
                break
        if flag:
            visited.append(x)
            visited_path.append([pos[curr], pos[x]])
            min_cost = min(min_cost, dfs(x) + distance(pos[curr], pos[x]))
            visited.pop()
            visited_path.pop()

    return min_cost


N = int(input())

pos = [list(map(int, input().split())) for _ in range(N)]

start = 0
visited_path = []
visited = [start]

print(dfs(start))
