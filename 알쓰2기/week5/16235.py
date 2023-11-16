# 나무 재테크

import sys
from collections import deque

input = sys.stdin.readline
N, M, K = map(int, input().split())

# A[r][c] - 겨울에 공급되는 양분의 양
A = [list(map(int, input().split())) for _ in range(N)]

# 양분
energy = [[5] * N for _ in range(N)]

# 나무들 - [age, row, col]
trees = []

# 죽은 나무들
dead_trees = []

for _ in range(M):
    r, c, age = map(int, input().split())
    trees.append([age, r - 1, c - 1])

trees = deque(sorted(trees))  # age순대로 정렬


# 봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다.
# 각각의 나무는 나무가 있는 1×1 크기의 칸에 있는 양분만 먹을 수 있다.
# 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다.
# 만약, 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.
def spring():
    for _ in range(len(trees)):
        age, r, c = trees.popleft()
        if energy[r][c] >= age:
            energy[r][c] -= age
            age += 1
            trees.append([age, r, c])
        else:
            dead_trees.append([age, r, c])


# 여름에는 봄에 죽은 나무가 양분으로 변하게 된다.
# 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다.
# 소수점 아래는 버린다.
def summer():
    global dead_trees
    for age, r, c in dead_trees:
        energy[r][c] += int(age / 2)
    dead_trees = []


# 가을에는 나무가 번식한다. 번식하는 나무는 나이가 5의 배수이어야 하며, 인접한 8개의 칸에 나이가 1인 나무가 생긴다.
dy = [0, -1, 0, 1, -1, -1, 1, 1]
dx = [1, 0, -1, 0, 1, -1, 1, -1]


def autumn():
    tmp = []
    for age, r, c in trees:
        if age % 5 == 0:
            for i in range(8):
                nr = r + dy[i]
                nc = c + dx[i]
                if 0 <= nr < N and 0 <= nc < N:
                    tmp.append([1, nr, nc])

    for tree in tmp:
        trees.appendleft(tree)


# 겨울에는 S2D2가 땅을 돌아다니면서 땅에 양분을 추가한다.
# 각 칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어진다.
def winter():
    for r in range(N):
        for c in range(N):
            energy[r][c] += A[r][c]


for _ in range(K):
    spring()
    summer()
    autumn()
    winter()

# 살아남은 나무의 개수를 출력한다.
print(len(trees))
