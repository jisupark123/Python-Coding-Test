# 합분해

# n개를 골랐을 때의 경우의 수 -> n+1 개를 골랐을 때의 경우의 수 각각의 합
# 4,2를 골랐을 때와 3,3을 골랐을 때 남은 경우의 수는 같다.
# 고른 횟수, 현재 값

N, K = map(int, input().split())

memo = [[-1 for _ in range(N + 1)] for _ in range(K + 1)]


def dfs(cnt, total):
    if total > N:
        return 0
    if memo[cnt][total] != -1:
        return memo[cnt][total]
    if cnt == K:
        return 1 if total == N else 0

    res = 0
    for n in range(N + 1):
        res += dfs(cnt + 1, total + n)
    memo[cnt][total] = res
    return res


print(dfs(0, 0) % 1000000000)
