# 보석 도둑

"""
- 담을 수 있는 무게가 적은 가방부터 채워나가야 함
- 보석은 가방에 담을 수 있으면서 가치가 가장 높은 순으로 채워나가야 함
- 다음 step의 가방으로 넘어갈수록 탐색할 보석의 space가 확장됨

- 각 가방에 담을 수 있는 모든 보석을 찾을 때 최소힙을 사용하고 (무게순)
- 각 가방에 넣을 수 있는 보석 중 가장 가치가 큰 보석을 찾을 때 최대힙을 사용헌다, (가치순)

가방은 무게순으로 정렬

1. i <- i 번째 가방, 담을 수 있는 무게 k[i]
2. 보석이 무게순으로 담긴 최소힙에서 무게가 k 이하인 보석을 꺼낸다.
3. 위에서 꺼낸 보석을 보석이 가치순으로 담긴 최대힙에 삽입한다.
4. 무게가 k보다 큰 보석이 나올 때까지 2,3을 반복
4. 최대힙에서 보석을 꺼내고 결과에 추가한다.
5. i <- i + 1

"""

import sys
import heapq

input = sys.stdin.readline


N, K = map(int, input().split())

jewels = [list(map(int, input().split())) for _ in range(N)]  # M, V
bags = [int(input()) for _ in range(K)]
bags.sort()


heapq.heapify(jewels)
max_heap = []

ans = 0

for k in bags:

    for _ in range(len(jewels)):
        if jewels[0][0] > k:  # 무게가 k 이하인 보석을 꺼낸다
            break
        m, v = heapq.heappop(jewels)
        heapq.heappush(max_heap, -v)

    if len(max_heap):  # 담을 수 있는 보석이 있을 경우
        ans += -heapq.heappop(max_heap)

print(ans)
