# 조합


def factorial(n):
    if n in [0, 1]:
        return 1
    return n * factorial(n - 1)


def combi(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))


n, r = map(int, input().split())

print(combi(n, r))
