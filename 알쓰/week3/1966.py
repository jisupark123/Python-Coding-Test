# 프린터 큐

import sys
from collections import deque

input = sys.stdin.readline


for _ in range(int(input())):
    N, M = map(int, input().split())
    queue = deque(map(lambda x: [x[0], int(x[1])], enumerate(input().split())))
    res = 0
    while queue:
        item = queue.popleft()
        if queue and item[1] < sorted(queue, key=lambda x: x[1], reverse=True)[0][1]:
            queue.append(item)
            continue
        else:
            res += 1
            if item[0] == M:
                print(res)
                break
