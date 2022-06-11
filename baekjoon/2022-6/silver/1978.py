# 소수 찾기

N = int(input())

nums = list(map(int, input().split()))

n = 1000
a = [False] + [False] + [True] * (n - 1)
primes = []

for i in range(2, n + 1):
    if a[i]:
        primes.append(i)
        for j in range(2 * i, n + 1, i):
            a[j] = False

res = 0

for num in nums:
    if num in primes:
        res += 1

print(res)
