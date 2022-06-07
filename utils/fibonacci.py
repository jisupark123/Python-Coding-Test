# 0 1 1 2 3 5 8 13 21 34


def fibo(n):
    if n in [0, 1]:
        return n
    array = [0 for i in range(n)]
    array[1] = 1
    for i in range(2, n):
        array[i] = array[i - 1] + array[i - 2]
    print(array)
    return array[n - 1]


print(fibo(10))
