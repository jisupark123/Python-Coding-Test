# 에디터
import sys
from collections import deque


input = sys.stdin.readline

left_stack = deque(input().strip())
right_stack = deque()

M = int(input())

for _ in range(M):
    command = input().strip()
    if command[0] == "L":
        if left_stack:
            right_stack.appendleft(left_stack.pop())
        else:
            continue
    elif command[0] == "D":
        if right_stack:
            left_stack.append(right_stack.popleft())
        else:
            continue
    elif command[0] == "B":
        if left_stack:
            left_stack.pop()
        else:
            continue
    elif command[0] == "P":
        left_stack.append(command[2])

print("".join(left_stack + right_stack))
