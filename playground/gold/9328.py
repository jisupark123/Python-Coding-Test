# 열쇠

import sys
from collections import deque

BLANK = "."
WALL = "*"
DOC = "$"


# 소문자인지 판별
def is_lower(s: str):
    return s == s.lower()


# 문자열 복사
def copy_string(s: str):
    return "".join([x for x in s])


# key set이 같거나 적고, 획득한 문서가 같거나 적다면 이미 방문했던 곳
def possible_update(arr, new_keys, new_docs_cnt):
    for keys, docs_cnt in arr:
        if new_keys in keys and new_docs_cnt <= docs_cnt:
            return False
    return True


input = sys.stdin.readline

h, w = map(int, input().split())

_map = [list(input().strip()) for _ in range(h)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

init_keys = sorted(input().strip())  # 처음부터 보유한 키 set
if init_keys == "0":
    init_keys = ""

entries = []  # 입구

for i in range(h):
    for j in range(w):
        if _map[i][j] != WALL:
            entries.append((i, j))

init = list(map(lambda x: (*x, init_keys), entries))

visited = [[[] for _ in range(w)] for _ in range(h)]

for y, x, keys, docs_cnt in init:
    visited[y][x].append((keys, docs_cnt))

# queue = deque(init)

ans = 0


def find_docs(y: int, x: int, keys: str, docs_cnt: int):
    pass
