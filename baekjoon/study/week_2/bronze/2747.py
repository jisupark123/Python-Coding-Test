# 피보나치 수


def fibo(n):
    if n in [0, 1]:
        return n
    array = [0 for i in range(n + 1)]
    array[1] = 1
    for i in range(2, n + 1):
        array[i] = array[i - 1] + array[i - 2]
    return array[n]


n = int(input())
print(fibo(n))
