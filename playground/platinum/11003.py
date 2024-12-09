# 최솟값 찾기


"""
방법 1 - 우선순위큐

1. 숫자와 인덱스를 우선순위큐에 push
2. 최솟값이 인덱스가 범위 안일 때까지 heappop
"""

# import heapq

# N, L = map(int, input().split())
# nums = list(map(int, input().split()))
# ans = []

# q = []

# for i in range(N):
#     heapq.heappush(q, (nums[i], i))

#     if i - L >= 0:
#         while q[0][1] <= i - L:
#             heapq.heappop(q)

#     ans.append(q[0][0])


# print(*ans)

"""
방법 2 - deque

deque의 첫번째 원소는 무조건 최솟값

1. 윈도우 사이즈보다 먼저 들어온 원소는 모두 삭제
2. 들어올 숫자보다 큰 원소는 모두 삭제 후 삽입 (사용할 일 없음) 
3. q 맨 앞의 원소 저장 (최솟값)
"""

from collections import deque

N, L = map(int, input().split())
nums = list(map(int, input().split()))
ans = []

q = deque()

for i in range(N):

    while q and q[0][0] <= i - L:
        q.popleft()

    while q and q[-1][1] > nums[i]:
        q.pop()

    q.append((i, nums[i]))
    ans.append(q[0][1])


print(*ans)
