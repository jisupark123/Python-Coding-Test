# 덱

import sys
from collections import deque

input = sys.stdin.readline


N = int(input())
deq = deque()

for _ in range(N):
    cmd = input().strip().split()
    if cmd[0] == "push_front":
        deq.appendleft(cmd[1])
    elif cmd[0] == "push_back":
        deq.append(cmd[1])
    elif cmd[0] == "pop_front":
        print(-1 if len(deq) == 0 else deq.popleft())
    elif cmd[0] == "pop_back":
        print(-1 if len(deq) == 0 else deq.pop())
    elif cmd[0] == "size":
        print(len(deq))
    elif cmd[0] == "empty":
        print(1 if len(deq) == 0 else 0)
    elif cmd[0] == "front":
        print(-1 if len(deq) == 0 else deq[0])
    elif cmd[0] == "back":
        print(-1 if len(deq) == 0 else deq[-1])
