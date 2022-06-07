# 빗물


def view_world(world):
    for w in world:
        print(w)


import sys

input = sys.stdin.readline

H, W = map(int, input().split())
blocks = list(map(int, input().split()))

# 2차원 세계 생성 (블록은 True, 빈공간은 False)
world = [[False for _ in range(W)] for _ in range(H)]
for w in range(W):
    for h in range(H):
        if h >= H - blocks[w]:
            world[h][w] = True

rain = 0
# 모든 좌표를 순회
# 좌표값이 False 이고 좌우에 True가 하나라도 있으면 1추가
# index(True)가 오류날 것을 대비해 try 구문 사용
for i in range(H):
    for j in range(W):
        try:
            if world[i][j] == False and world[i].index(True) < j < (W - 1) - world[i][
                ::-1
            ].index(True):
                rain += 1
        except:
            continue
print(rain)

# print(floor.index(True), end="")
# print(f, end="")
# print((len(floor) - 1) - floor[::-1].index(True))
# world = [[True if h == H else False for _ in range(W)] for h in range(H + 1)]
