# 에라스토테네스의 체
def eratosthenes():
    n = 11  # 체크할 범위
    a = [False] + [False] + [True] * (n - 1)  # 0,1은 소수가 아니므로 False
    primes = []  # 범위 안의 소수를 저장할 리스트

    for i in range(2, n + 1):
        if a[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                a[j] = False
    return primes


import math

# 소수 판별 함수
def is_prime_number(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
