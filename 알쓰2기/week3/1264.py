# 모음의 개수

import sys

input = sys.stdin.readline
target = ["a", "e", "i", "o", "u"]

while True:
    w = input().strip()
    if w == "#":
        break
    res = 0
    for s in w:
        if s.lower() in target:
            res += 1
    print(res)
