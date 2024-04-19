# 집합

# 비트마스킹으로 해결

import sys

input = sys.stdin.readline

S = 0


for _ in range(int(input())):
    temp = input().strip().split(" ")
    cmd = temp[0]
    if len(temp) == 2:
        n = int(temp[1])

    if cmd == "add":
        S |= 1 << (n - 1)

    elif cmd == "remove":
        S &= ~(1 << (n - 1))

    elif cmd == "check":
        if S & 1 << (n - 1):
            print(1)
        else:
            print(0)

    elif cmd == "toggle":
        S ^= 1 << (n - 1)

    elif cmd == "all":
        S = 2**20 - 1

    elif cmd == "empty":
        S = 0
