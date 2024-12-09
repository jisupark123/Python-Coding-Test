# 최솟값 찾기


"""
방법 2 - 우선순위큐

1. 숫자와 인덱스를 우선순위큐에 push
2. 최솟값이 인덱스가 범위 안일 때까지 heappop
"""

import heapq

N, L = map(int, input().split())
nums = list(map(int, input().split()))
ans = []

q = []

for i in range(N):
    heapq.heappush(q, (nums[i], i))

    if i - L >= 0:
        while q[0][1] <= i - L:
            heapq.heappop(q)

    ans.append(q[0][0])


print(*ans)
