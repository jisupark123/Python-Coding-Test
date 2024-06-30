# 호숫가의 개미굴

"""
1. 모든 쪽방에 개미 넣기
2. 쪽방이 아닌 방에 순차적으로 개미 넣기 (그리디)

- 개미굴의 시작과 끝이 연결되어 있음
"""

import sys

input = sys.stdin.readline

n = int(input())
c = list(map(int, input().split()))

# 개미를 넣으면 p = False
# 안넣으면 p = True

# 처음에 넣는 경우와 안넣는 경우 중 max를 선택

ans1 = sum(c)

p = True

for i in range(n - 1):
    if p and c[i] == 0:
        ans1 += 1
        p = False
    else:
        p = True

if p and c[-1] == 0 and c[0] != 0:
    ans1 += 1

ans2 = sum(c)
p = True

for i in range(1, n):
    if p and c[i] == 0:
        ans2 += 1
        p = False
    else:
        p = True


print(max(ans1, ans2))
