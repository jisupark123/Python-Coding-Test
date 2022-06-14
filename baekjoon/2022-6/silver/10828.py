# 스택

import sys

input = sys.stdin.readline


N = int(input())
stack = []

for _ in range(N):
    s = input().strip().split()
    command = s[0]
    if len(s) != 1:
        x = s[1]
    if command == "push":
        stack.append(x)
    elif command == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        print(1 if len(stack) == 0 else 0)
    elif command == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
