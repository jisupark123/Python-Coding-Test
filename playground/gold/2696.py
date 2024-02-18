# 중앙값 구하기

"""
우선순위큐 2개를 활용 
집합을 반으로 나눠서 각각 최대힙/최소힙으로 관리

최대힙 A -> 작은 수들의 집합
최소힙 B -> 큰 수들의 집합

A를 거꾸로 한 배열과 B를 합치면 정렬된 수가 나온다.
A와 B는 항상 같은 원소의 개수로 관리한다. (홀수라면 B의 원소를 하나 많게 관리한다)

알고리즘 상세


1. 수 n이 들어오면 n과 A의 최댓값와 B의 최솟값을 비교한다.
-> 만약 A나 B가 비어있을 것을 대비해서 A에 -10001을, B에 10001을 초기값으로 넣어놓는다.

2. n이 A의 최댓값보다 작거나 같다면 
-> 홀수일 시 A의 최댓값을 출력한다.
-> A와 B의 길이가 같다면 n을 A에 넣고 A의 최댓값을 B에 넣는다.
-> A보다 B의 길이가 길다면 n을 A에 넣는다.

3. n이 B의 최솟값보다 작거나 같다면 
-> 홀수일 시 n을 출력한다.
-> A와 B의 길이가 같다면 n을 B에 넣는다.
-> A보다 B의 길이가 길다면 n을 A에 넣는다.

4. n이 B의 최솟값보다 크다면 
-> 홀수일 시 A의 최솟값을 출력한다.
-> A와 B의 길이가 같다면 n을 B에 넣는다.
-> A보다 B의 길이가 길다면 n을 B에 넣고 B의 최솟값을 A에 넣는다.
"""

import sys
import heapq

input = sys.stdin.readline


class MaxHeap:
    def __init__(self):
        self.queue = []

    def heappush(self, x):
        heapq.heappush(self.queue, -x)

    def heappop(self):
        return -heapq.heappop(self.queue)

    def max(self):
        return -self.queue[0]

    def __len__(self):
        return len(self.queue)


class MinHeap:
    def __init__(self):
        self.queue = []

    def heappush(self, x):
        heapq.heappush(self.queue, x)

    def heappop(self):
        return heapq.heappop(self.queue)

    def min(self):
        return self.queue[0]

    def __len__(self):
        return len(self.queue)


T = int(input())

for _ in range(T):

    N = int(input())
    nums = []
    for _ in range(N // 10 + min(1, N % 10)):
        nums.extend(map(int, input().split()))

    A = MaxHeap()  # 최대힙
    A.heappush(-float("inf"))

    B = MinHeap()  # 최소힙
    B.heappush(float("inf"))

    ans = []

    for i in range(N):
        n = nums[i]
        max_a = A.max()
        min_b = B.min()

        # 2. n이 A의 최댓값보다 작거나 같다면
        # -> 홀수일 시 A의 최댓값을 출력한다.
        # -> A와 B의 길이가 같다면 n을 A에 넣고 A의 최댓값을 B에 넣는다.
        # -> A보다 B의 길이가 길다면 n을 A에 넣는다.

        if n <= max_a:

            if (i + 1) % 2 == 1:
                ans.append(max_a)

            if len(A) == len(B):
                A.heappush(n)
                B.heappush(A.heappop())
            else:
                A.heappush(n)

        # 3. n이 B의 최솟값보다 작거나 같다면
        # -> 홀수일 시 n을 출력한다.
        # -> A와 B의 길이가 같다면 n을 B에 넣는다.
        # -> A보다 B의 길이가 길다면 n을 A에 넣는다.

        elif n <= min_b:

            if (i + 1) % 2 == 1:
                ans.append(n)
            if len(A) == len(B):
                B.heappush(n)
            else:
                A.heappush(n)

        # 4. n이 B의 최솟값보다 크다면
        # -> 홀수일 시 A의 최솟값을 출력한다.
        # -> A와 B의 길이가 같다면 n을 B에 넣는다.
        # -> A보다 B의 길이가 길다면 n을 B에 넣고 B의 최솟값을 A에 넣는다.

        else:
            if (i + 1) % 2 == 1:
                ans.append(min_b)

            if len(A) == len(B):
                B.heappush(n)
            else:
                B.heappush(n)
                A.heappush(B.heappop())

    print(len(ans))

    # for i in range(N // 10 + min(1, N % 10)):
    #     print(*ans[i * 10 : i * 10])

    for i in range(len(ans)):
        if i != 0 and i % 10 == 0:
            print()
        print(ans[i], end=" ")
