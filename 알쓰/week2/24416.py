# 알고리즘 수업 - 피보나치 수 1


n = int(input())
memo = [0] * 41

basic_cnt = 0
dp_cnt = 0


def basic_fib(n):
    global basic_cnt
    if n == 1 or n == 2:
        basic_cnt += 1
        return 1
    if memo[n] != 0:
        basic_cnt += memo[n]
        return memo[n]
    else:
        res1 = basic_fib(n - 1)
        res2 = basic_fib(n - 2)
        memo[n - 1] = res1
        memo[n - 2] = res2
        return res1 + res2


def dp_fib(n):
    if n < 3:
        return n
    global dp_cnt
    lst = [1, 1]
    for _ in range(2, n):
        lst.append(lst[-2] + lst[-1])
        dp_cnt += 1
    return lst[-1]


basic_fib(n)
dp_fib(n)

print(basic_cnt, dp_cnt)
