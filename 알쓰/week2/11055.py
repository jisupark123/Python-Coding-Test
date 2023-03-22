# 가장 큰 증가하는 부분 수열
# i에서의 정답은
# i까지의 합 + i 부터의 합
# i 부터의 합

N = int(input())
lst = list(map(int, input().split()))

memo = [None] * N
res = []


def dfs(prev_sum: int, curr_idx: int):
    if memo[curr_idx] != None:
        return prev_sum + memo[curr_idx]
    _max = 0
    for i in range(curr_idx + 1, N):
        if lst[curr_idx] < lst[i]:
            front = dfs(lst[curr_idx], i)  # i부터의 값
            _max = max(front, _max)
    if _max == 0:
        memo[curr_idx] = lst[curr_idx]
        return prev_sum + lst[curr_idx]

    memo[curr_idx] = _max
    return prev_sum + _max


for i in range(N):
    dfs(0, i)

print(max(memo))
