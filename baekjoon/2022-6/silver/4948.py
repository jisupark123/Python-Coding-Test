# 베르트랑 공준


def eratosthenes(n):
    a = [False] + [False] + [True] * (n - 1)  # 0,1은 소수가 아니므로 False
    primes = []  # 범위 안의 소수를 저장할 리스트

    for i in range(2, n + 1):
        if a[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                a[j] = False
    return primes


while True:
    n = int(input())
    if n == 0:
        break
    primes = eratosthenes(2 * n)
    print(len([x for x in primes if x > n]))
