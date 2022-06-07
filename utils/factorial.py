# 팩토리얼 구하기
# n!


def factorial(n):
    if n in [0, 1]:
        return 1
    return n * factorial(n - 1)
