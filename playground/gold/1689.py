# 겹치는 선분

"""
스위핑 알고리즘

- 좌표와 시작점, 끝점의 정보를 리스트로 표현 ([좌표, start/end])
- 좌표를 기준으로 정렬, 좌표가 같다면 끝점을 우선 정렬
- 정렬된 좌표를 for문을 돌면서 각 순간에 선분이 몇개 겹치는지 구하기 (start 좌표가 나오면 1더하고 end면 1빼고)
"""

import sys

input = sys.stdin.readline

N = int(input())

lines = []

for _ in range(N):
    a, b = map(int, input().split())
    lines.append([a, 1])  # 시작점
    lines.append([b, -1])  # 끝점

lines.sort()

ans = 0
line_cnt = 0

for line in lines:
    line_cnt += line[1]
    ans = max(ans, line_cnt)

print(ans)
