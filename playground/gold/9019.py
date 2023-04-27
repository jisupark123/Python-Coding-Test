# DSLR

import sys
from collections import deque

input = sys.stdin.readline

T = int(input())


def calc(n: int, cmd: str) -> int:
    if cmd == "D":
        res = n * 2
        return res if res < 10000 else res % 10000
    if cmd == "S":
        res = n - 1
        return res if n != 0 else 9999
    if cmd == "L":
        front = n % 1000
        back = n // 1000
        return front * 10 + back
    if cmd == "R":
        front = n % 10
        back = n // 10
        return front * 1000 + back


for _ in range(T):
    a, b = map(int, input().split())
    visit = [False] * 10000

    queue = deque()
    queue.append((a, ""))
    visit[a] = True

    while queue:
        num, cmd = queue.popleft()
        if num == b:
            print(cmd)
            break
        for c in "DSLR":
            next_num = calc(num, c)
            if not visit[next_num]:
                visit[next_num] = True
                queue.append((next_num, cmd + c))
