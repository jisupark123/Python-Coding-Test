# 미로 만들기
import copy

S = int(input())
move = input()

# 방향 - 남서북동
direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]

# 움직임을 x,y 좌표로 모두 저장 - 처음은 원점
moving_points = [(0, 0)]

# 홍준이가 보고있는 방향 (direction[d]) - 처음은 남쪽
d = 0

for m in move:
    if m == "F":
        moving_points.append(
            tuple(map(lambda x: sum(x), zip(moving_points[-1], direction[d % 4])))
        )
    elif m == "R":  # 오른쪽으로 전환
        d += 1
    else:  # 왼쪽으로 전환
        d += 3

moving_points = set(moving_points)
x_lst = [x[0] for x in moving_points]
y_lst = [y[1] for y in moving_points]
max_x = max(x_lst)
min_x = min(x_lst)
max_y = max(y_lst)
min_y = min(y_lst)


# 미로의 크기
x_width = abs(max_x - min_x) + 1
y_width = abs(max_y - min_y) + 1

maze = [["#" for _ in range(x_width)] for _ in range(y_width)]


def draw():
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            res = copy.deepcopy(maze)
            try:
                for point in moving_points:
                    new_point = [i + point[0], j + point[1]]
                    if new_point[0] < 0 or new_point[1] < 0:
                        raise
                    res[new_point[0]][new_point[1]] = "."
                return res
            except:
                continue


res = draw()

for i in res:
    for j in i:
        print(j, end="")
    print()
