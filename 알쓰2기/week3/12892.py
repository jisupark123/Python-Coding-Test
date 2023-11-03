# 생일 선물

"""
1. 가격이 낮은 순서대로 정렬한다.
2. 포인터 i,j를 생성한다.
3. gifts[j] - gifts[i] 의 가격이 D를 초과하기 바로 전까지 j를 오른쪽으로 이동시키고 만족도의 합을 구한다.
4. i를 1이동시키고 3,4를 반복한다.
"""

import sys

input = sys.stdin.readline

N, D = map(int, input().split())
gifts = [list(map(int, input().split())) for _ in range(N)]

res = 0
