# 캐슬 디펜스

"""
궁수의 위치 각각마다 제거할 수 있는 적의 최대 수를 계산한다.
모든 적들과 궁수의 위치는 리스트에 좌표로 관리한다.
"""

import sys

input = sys.stdin.readline

N, M, limit = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

res = 0


def get_max_enemy(combi):
    archers = [(N, x) for x in combi]  # 궁수 인덱스
    enemies = set()  # (row,col) 적 인덱스
    dead_enemies_cnt = 0

    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                enemies.add((i, j))

    while len(enemies):
        min_dist_enemies = [
            (sys.maxsize, 0, 0)
        ] * 3  # (distance,row,col) 궁수 3명 각각 가장 가까운 적

        for enemy in enemies:  # 모든 적들을 순회
            for i in range(3):  # 궁수 3명과 각각 비교
                # 적과 궁수의 거리 구하기
                distance = abs(enemy[0] - archers[i][0]) + abs(enemy[1] - archers[i][1])

                # 궁수 3명 각각 가장 가까운 적 구하기
                # 거리가 공격 거리 제한보다 작거나 같고
                # (거리가 더 가깝거나
                # 거리가 같고 더 왼쪽에 위치해있으면)
                if distance <= limit and (
                    distance < min_dist_enemies[i][0]
                    or (
                        distance == min_dist_enemies[i][0]
                        and enemy[1] < min_dist_enemies[i][2]
                    )
                ):
                    min_dist_enemies[i] = (distance, enemy[0], enemy[1])

        dead_enemies = set()
        for enemy in min_dist_enemies:
            if enemy[0] != sys.maxsize:
                dead_enemies.add((enemy[1], enemy[2]))
        dead_enemies_cnt += len(dead_enemies)
        new_enemies = set()
        for enemy in enemies:
            if enemy not in dead_enemies and enemy[0] != N - 1:
                new_enemies.add((enemy[0] + 1, enemy[1]))
        enemies = new_enemies

    global res
    res = max(res, dead_enemies_cnt)


for i in range(M - 2):
    for j in range(i + 1, M - 1):
        for k in range(j + 1, M):
            get_max_enemy((i, j, k))
print(res)
