# 캐슬 디펜스

"""
궁수의 위치 각각마다 제거할 수 있는 적의 최대 수를 계산한다.
모든 적들과 궁수의 위치는 리스트에 좌표로 관리한다.
"""

import sys
from itertools import combinations

input = sys.stdin.readline

N, M, limit = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]


def get_max_enemy(combi):
    archers = [(N, x) for x in combi]
    enemies = []  # (row,col)
    dead_enemies = set()
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                enemies.append([i, j])

    min_dist_enemies = [(sys.maxsize, 0, 0)] * 3  # (distance,row,col)

    for enemi in enemies:  # 모든 적들을 순회
        if enemi in dead_enemies:
            continue
        for i in range(3):  # 궁수 3명과 각각 비교
            # 적과 궁수의 거리 구하기
            distance = abs(enemi[0] - archers[i][0]) + abs(enemi[1] - archers[i][1])

            # 궁수 3명 각각 가장 가까운 적 구하기
            # 거리가 공격 거리 제한보다 작거나 같고
            # (거리가 더 가깝거나
            # 거리가 같고 더 왼쪽에 위치해있으면)
            if distance <= limit and (
                distance < min_dist_enemies[i][0]
                or (
                    distance == min_dist_enemies[i][0]
                    and enemi[1] < min_dist_enemies[i][2]
                )
            ):
                min_dist_enemies[i] = (distance, enemi[0], enemi[1])

    for enemi in min_dist_enemies:
        if enemi[0] != sys.maxsize:
            dead_enemies.add((enemi[1], enemi[2]))


res = 0

# for c in combinations(range(M), 3):
#     get_max_enemy(c)
get_max_enemy((0, 1, 2))
