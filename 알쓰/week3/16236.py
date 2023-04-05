# 아기 상어


import sys
from collections import deque

input = sys.stdin.readline


# 상어 위치 세팅 & 맵 생성
def set_baby_shark_pos():
    global curr_pos
    for i in range(N):
        for j in range(N):
            if space[i][j] == 9:
                curr_pos = (i, j)
                space[i][j] = 0
                return


"""
어느 물고기를 잡아먹을지 결정하는 함수
fish_A를 잡아먹어야 한다면 True, 반대면 False를 리턴
1. 거리가 가까운 물고기를 잡아먹는다
2. 거리가 같다면 위에 있는 물고기, 같다면 가장 왼쪽에 있는 물고기를 잡아먹는다.
"""


def compare_fish(fish_A, fish_B) -> bool:
    if fish_A["distance"] < fish_B["distance"]:
        return True
    if fish_A["distance"] > fish_B["distance"]:
        return False
    if fish_A["idx"][0] < fish_B["idx"][0]:
        return True
    if fish_A["idx"][0] > fish_B["idx"][0]:
        return False
    if fish_A["idx"][1] < fish_B["idx"][1]:
        return True
    if fish_A["idx"][1] > fish_B["idx"][1]:
        return False


"""
다음에 먹을 물고기의 위치와 걸리는 시간을 리턴하는 함수
먹을 물고기가 없다면 (-1,-1)를 리턴한다
다음에 먹을 물고기의 위치 -> 아기상어보다 레벨이 낮고 거리가 가장 가까운 물고기
거리가 같다면 -> 가장 위에 있는 물고기 -> 가장 왼쪽에 있는 물고기
아기상어보다 레벨이 더 높다면 지나갈 수 없다.


구현 방법 -> bfs
큐를 생성한다. 초기값은 아기 상어의 현재 위치
각각의 인덱스에 방문처리를 할 NxN 리스트 생성
min_fish <- {idx:(-1,-1), dist: 1e9} 가장 가까운 물고기의 인덱스, 거리
1. 큐에서 위치 (i,j)를 꺼낸다.
2. 현재 위치에 물고기가 있다면 min_fish.dist 와 비교 -> 최신화
3. 상하좌우 4방향에 대해서 다음 위치를 구한다. (next_i,next_j)
4. 다음 위치에 대해서 검사
4.a 인덱스 검사
4.b 다음 위치를 방문했었는지(방문 안 한 경우만 진행)
4.c 다음 위치에 자신보다 레벨이 높은 상어가 있는지
5. 가능하다면 방문 처리하고 큐에 다음 위치 추가
6. 큐가 비었다면 min_fish.idx, time 리턴
"""


def get_min_fish():
    # 최단 거리의 물고기를 저장
    # idx -> 인덱스 | dist -> 거리
    min_fish = {"idx": (-1, -1), "distance": 1e9}
    visit = [[False for _ in range(N)] for _ in range(N)]

    # 큐의 초기값 -> 현재 위치, 총 거리
    queue = deque([[curr_pos[0], curr_pos[1], 0]])
    while queue:
        pos_y, pos_x, dist = queue.popleft()

        # 큐에서 빼낸 위치에 아기 상어보다 레벨이 낮은 물고기가 있다면
        # min_fish와 비교 -> 업데이트
        if (
            space[pos_y][pos_x] != 0
            and space[pos_y][pos_x] < level
            and compare_fish({"idx": (pos_y, pos_x), "distance": dist}, min_fish)
        ):
            min_fish["idx"] = (pos_y, pos_x)
            min_fish["distance"] = dist

        # 상하좌우 4곳을 각각 탐색
        for d in direction:
            next_pos_y = pos_y + d[0]
            next_pos_x = pos_x + d[1]
            if (
                # 인덱스 검사
                0 <= next_pos_y < N
                and 0 <= next_pos_x < N
                # 방문하지 않은 곳이라면
                and not visit[next_pos_y][next_pos_x]
                # 아기 상어보다 레벨이 높은 물고기가 있다면 접근 불가
                and space[next_pos_y][next_pos_x] <= level
            ):
                # 방문처리
                visit[next_pos_y][next_pos_x] = True
                # 큐에 다음 방문할 곳 추가
                queue.append((next_pos_y, next_pos_x, dist + 1))

    # (잡아먹을 물고기 y, 잡아먹을 물고기 x, 걸린 시간) return
    next_fish_y = min_fish["idx"][0]
    next_fish_x = min_fish["idx"][1]
    return (next_fish_y, next_fish_x, min_fish["distance"])


N = int(input())


space = [list(map(int, input().split())) for _ in range(N)]  # 공간의 상태
direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # 상하좌우

curr_pos: tuple[int] = ()  # 아기 상어의 위치
level = 2  # 아기 상어의 레벨
exp = 0  # 경험치, 레벨만큼 쌓이면 레벨이 1 증가하고 경험치는 초기화된다.
time = 0  # 아기 상어가 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간
set_baby_shark_pos()  # 아기 상어 위치 세팅


"""
1. 먹을 수 있는 레벨의 상어 중 거리가 가장 최소인 상어를 고른다.
2. 상어를 그 자리로 이동시키고 먹이가 된 상어를 삭제한다.
3. 먹을 수 있는 상어가 없다면 종료한다.
"""


while True:
    next_fish = get_min_fish()  # 잡아먹을 물고기
    if next_fish[0] == -1:  # 잡아먹을 물고기가 없다면 종료
        break

    # 잡아먹은 물고기가 있던 곳은 빈곳으로 바꾸기
    space[next_fish[0]][next_fish[1]] = 0

    # 잡아먹은 시간 결과값에 추가
    time += next_fish[2]

    # 아기상어 위치 업데이트
    curr_pos = (next_fish[0], next_fish[1])

    # 경험치 1 추가
    exp += 1

    # 경험치가 레벨과 같아지면 레벨 1 추가, 경험치 초기화
    if level == exp:
        level += 1
        exp = 0

print(time)  # 총 시간을 출력
