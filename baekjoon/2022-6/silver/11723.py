# 집합

import sys

input = sys.stdin.readline

S = set()
M = int(input())

for _ in range(M):
    cmd = input().strip().split()
    if len(cmd) == 2:
        x = int(cmd[1])
    if cmd[0] == "add":
        S.add(x)
    elif cmd[0] == "remove":
        try:
            S.remove(x)
        except:
            continue
    elif cmd[0] == "check":
        if x in S:
            print(1)
        else:
            print(0)
    elif cmd[0] == "toggle":
        try:
            S.remove(x)
        except:
            S.add(x)
    elif cmd[0] == "all":
        S = set(range(1, 21))
    elif cmd[0] == "empty":
        S = set()
