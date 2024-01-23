# 거스름돈

n = int(input())


def answer():
    if n < 5:
        return n // 2 if n % 2 == 0 else -1
    if n % 5 == 0:
        return n // 5
    if n % 5 % 2 == 0:
        return (n // 5) + (n % 5 // 2)
    if (n % 5 - 5) % 2 == 0:
        return (n // 5 - 1) + ((n % 5 + 5) // 2)

    return -1


print(answer())
