# 피리 부는 사나이

"""
서로 연결되어 있는 좌표끼리 집합을 구성하고 각 집합 당 1개의 Safe Zone을 설치 (집합의 개수가 정답)

NxM 배열에 같은 집합을 같은 숫자로 마킹하는 방식을 사용
"""

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

_map = [input().strip() for _ in range(N)]

making = [[-1] * M for _ in range(N)]

hash = 0

direction = {"D": [1, 0], "U": [-1, 0], "L": [0, -1], "R": [0, 1]}

for i in range(N):
    for j in range(M):
        if making[i][j] == -1:

            nodes = [(i, j)]
            making[i][j] = hash

            while True:
                y, x = nodes[-1]
                d = direction[_map[y][x]]
                ny, nx = y + d[0], x + d[1]

                # 같은 집합일 경우 중단
                if making[ny][nx] == making[y][x]:
                    break

                # 빈 곳일 경우 집합에 추가
                if making[ny][nx] == -1:
                    making[ny][nx] = hash
                    nodes.append((ny, nx))

                # 다른 집합일 경우, 집합을 하나로 합치기
                # 탐색했던 좌표들을 해당 집합의 hash로 통일
                else:
                    for py, px in nodes:
                        making[py][px] = making[ny][nx]
                    break

            hash += 1

ans = set()

for i in range(N):
    for j in range(M):
        ans.add(making[i][j])

print(len(ans))
