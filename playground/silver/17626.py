# Four Squares

"""
25
4 3
1 2 2 4

"""

"""
숫자 N의 경우의 수
-> sol(N, 4) // 4는 횟수 제한
-> sol(N - (1**2), 3) + sol(N - (2**2), 3) + sol(N - (3**2), 3) + ... + sol(N - ((N**0.5)**2), 3)
"""

import math

N = int(input())

limit = math.ceil(N**0.5)

# memo = [[-1] * 5] * (N + 1)


def sol(n, cnt):
    if n == 0:
        return 1
    if cnt == 0:
        return 0
    res = 0
    for i in range(1, limit):
        r = sol(n - (i**2), cnt - 1)
        if r != 0:
            print(n, cnt, i)
        res += r

    return res


print(sol(N, 4))
