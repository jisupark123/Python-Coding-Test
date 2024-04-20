# 계단 수

"""
- 길이가 N이고 0부터 9까지 숫자가 모두 등장하는 계단 수 = s()

- a부터 시작하고 0부터 9까지 숫자가 모두 등장하는 길이가 n인 계단 수 = f(a, n, bit(각 숫자 방문 여부))

- s() = sum(f(a, n, bit) for a in 1~9) = sum(f(a, n-1, 변경된 bit) for a in (a+1, a-1))
"""

N = int(input())


# axis 0 - 시작 숫자
# axis 1 - 계단 수 길이
# axis 2 - bit(각 숫자 방문 여부)
# value - 경우의 수
dp = [[[-1] * (2**10) for _ in range(N + 1)] for _ in range(10)]


def dfs(a, n, visited):
    if n == 1:
        if visited == 2**10 - 1:
            return 1
        else:
            return 0

    if dp[a][n][visited] != -1:
        return dp[a][n][visited]

    s = 0
    for na in (a - 1, a + 1):
        if 0 <= na <= 9:
            tmp = dfs(na, n - 1, visited | (1 << na))
            dp[na][n - 1][visited | (1 << na)] = tmp
            s += tmp

    return s


def solution(n):
    return sum((dfs(a, n, 1 << a) for a in range(1, 10)))


print(solution(N) % 1000000000)
