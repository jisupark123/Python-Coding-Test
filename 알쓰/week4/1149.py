# RGB거리

# 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

# 모든 집을 칠하는 비용의 최솟값 -> n번 집에 각각 RGB를 칠했을 때 중의 최솟값
# i번째 집에서 c 색깔의 집을 선택했을 때의 최솟값을 저장

import sys

sys.setrecursionlimit(10000000)

input = sys.stdin.readline

N = int(input())
values = [tuple(map(int, input().split())) for _ in range(N)]

max_total = 1000 * 1000

# i번째 집에서 c 색깔의 집을 선택했을 때의 최솟값을 저장
memo = [[-1 for _ in range(3)] for _ in range(N)]


def dfs(i, total, prev_color):
    if i == N:
        return total
    # if total > memo[i][prev_color]:
    #     print(i)
    #     return memo[i][prev_color]
    res = []
    for color in range(3):
        if color != prev_color:
            if memo[i][color] != -1:
                res.append([memo[i][color], color])
            else:
                min_value = dfs(i + 1, values[i][color], color)
                memo[i][color] = min_value
                res.append([min_value, color])
    min_res = min(res)
    return total + min_res[0]


print(dfs(0, 0, -1))
