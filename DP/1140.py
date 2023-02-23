# RGB거리

"""
N에서의 최솟값은 N-1(R)과 다른 값인 G와 B 둘 중 하나를 선택했을 때의 최솟값
N과 N+1의 조합을 찾아서 가장 최소인 조합(N, N+1) 중 N을 택하면 됨
26 40 83
49 60 57
89 99 13
"""

import sys

input = sys.stdin.readline

N = int(input())
costs = [tuple(map(int, input().split())) for _ in range(N)]
costs.append((0, 0, 0))

res = 0
previous_rgb = -1

for i in range(len(costs) - 1):

    min_value = 3000
    min_n = 0
    for a in range(3):
        for b in range(3):
            if a == b or a == previous_rgb:
                continue
            if costs[i][a] + costs[i + 1][b] < min_value:
                min_value = costs[i][a] + costs[i + 1][b]
                min_n = a
    res += costs[i][min_n]
    previous_rgb = min_n

print(res)
