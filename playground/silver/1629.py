a, b, c = map(int, input().split())


def compute(n):
    if n == 1:
        return a % c
    tmp = compute(n // 2)
    return (tmp**2) % c if n % 2 == 0 else (tmp**2 * a) % c


print(compute(b))
