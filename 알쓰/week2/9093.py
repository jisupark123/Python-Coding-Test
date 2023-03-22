# 단어 뒤집기

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    print(" ".join(map(lambda x: x[::-1], input().strip().split(" "))))
