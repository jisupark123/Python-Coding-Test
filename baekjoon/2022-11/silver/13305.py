# 주유소

"""

1. 지났던 주유소 중 최솟값을 m에 저장한다.
2. for문을 돌면서 m * road[i]를 결과값에 더한다.

"""


N = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))


res = 0
m = costs[0]

for i in range(N - 1):
    if costs[i] < m:
        m = costs[i]
    res += m * roads[i]

print(res)
