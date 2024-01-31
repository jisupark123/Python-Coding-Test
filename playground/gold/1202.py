# 보석 도둑

"""
방법: 그리디 알고리즘 & 이분 탐색
- 가치가 높은 순으로 가방을 채워나감
- 가능한 것 중에 최대 무게가 가장 작은 가방을 채워야 한다. -> how?
- 이분 탐색으로 찾기 
-> 못 찾을 경우를 대비해서 탐색 도중 최댓값을 갱신시킨다.
-> 보석 무게와 같거나 클 때만 최댓값 갱신

-----------------------------------------------------------

방법: 그리디 알고리즘 & 해시 테이블 & 이분 탐색
- 가치가 높은 순으로 가방을 채워나감
- 가능한 것 중에 최대 무게가 가장 작은 가방을 채워야 한다. -> how?
- 

해시 테이블 -
> key:무게, value: 인덱스
> 1. 양옆으로 인접한 key쌍을 저장
> 2. 각 무게에 해당하는 가방의 개수를 저장

이분 탐색 - 
> 
"""

import sys

input = sys.stdin.readline


def find(x):  # 이분 탐색으로 x or x와 가장 가까운 item 탐색
    res = None  # x와 같은 가방의 인덱스
    near_res = None  # x와 가장 가까운 가방의 인덱스

    start = 0
    end = K - 1


N, K = map(int, input().split())

jewels = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

jewels.sort(key=lambda x: (x[1], x[0]), reverse=True)
bags.sort()
