# 소수


def eratosthenes(n):
    a = [False] + [False] + [True] * (n - 1)  # 0,1은 소수가 아니므로 False
    primes = []  # 범위 안의 소수를 저장할 리스트

    for i in range(2, n + 1):
        if a[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                a[j] = False
    return primes


M = int(input())
N = int(input())

all_nums = eratosthenes(N)
nums = [x for x in all_nums if x >= M]

if len(nums) == 0:
    print(-1)
else:
    print(sum(nums))
    print(min(nums))
