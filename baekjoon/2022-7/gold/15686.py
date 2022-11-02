# 치킨 배달

from itertools import combinations
from sys import stdin


input = stdin.readline


def all_chicken_distance(chickens: list):
    def nearest_chicken(r, c):  # 가장 가까운 치킨집의 거리를 구하는 함수
        min_distance = 1e9
        for chicken in chickens:
            distance = abs(r - chicken[0]) + abs(c - chicken[1])
            min_distance = min(distance, min_distance)

        return min_distance

    res = 0
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                res += nearest_chicken(i, j)
    return res


N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]
chickens = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chickens.append((i, j))


res = 1e9

for c in list(combinations(range(len(chickens)), M)):
    new_chickens = [chickens[x] for x in c]
    chicken_distance = all_chicken_distance(new_chickens)
    res = min(chicken_distance, res)

print(res)
