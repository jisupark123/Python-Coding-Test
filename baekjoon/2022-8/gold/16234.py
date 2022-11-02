# 인구 이동

import sys

sys.setrecursionlimit(10000)

direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # 상하좌우


def get_alliance() -> list[list[tuple[int]]]:

    """
    dfs()
    1. 이미 방문했다면 종료
    2. 방문 처리
    #
    3. 상하좌우의 땅을 검사한다ㄴ
    - 이미 연합에 속해있으면 진행X
    - 인덱스를 벗어나면 진행X
    - L,R 사이가 아니라면 진행X
    4. 위의 검사를 통과하면 재귀함수 호출
    """

    def dfs(i: int, j: int):

        if visited[i][j] == 1:  # 방문했었다면 종료
            return
        visited[i][j] = 1  # 방문 처리

        for d in direction:
            new_i = i + d[0]
            new_j = j + d[1]

            # 인덱스를 벗어나면 종료
            if new_i < 0 or new_i >= N or new_j < 0 or new_j >= N:
                continue

            # L 이상 R 이하가 아니라면 종료
            if not L <= abs(world[i][j] - world[new_i][new_j]) <= R:
                continue

            # 이미 연합에 속해있으면 종료
            if (new_i, new_j) in alliance:
                continue
            alliance.append((new_i, new_j))
            dfs(new_i, new_j)

    res: list[list[tuple[int]]] = []
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                continue
            alliance: list[tuple[int]] = []
            dfs(i, j)
            if len(alliance):
                res.append(alliance)

    return res


input = sys.stdin.readline

N, L, R = map(int, input().split())

world = [list(map(int, input().split())) for _ in range(N)]

day = 0


# 1. 연합 구하기
# 2. 연합끼리 인구 이동(평균)
# 3. 이동이 없다면 종료
# 4. day += 1
while True:
    change = False
    alliances = get_alliance()
    for alliance in alliances:
        total = 0

        # 합 구하기
        for country in alliance:
            total += world[country[0]][country[1]]

        # 평균
        average = int(total / len(alliance))

        # 실제로 인구 이동
        for country in alliance:
            world[country[0]][country[1]] = average
            change = True

    if not change:  # 이동이 없다면 종료
        break

    day += 1


print(day)
