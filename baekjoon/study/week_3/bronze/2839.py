# 설탕 배달


N = int(input())


def sugar(N):
    res = 0
    while True:
        if N % 5 == 0:
            res += N // 5
            return res
        elif N == 0:
            return res
        elif N < 0:
            return -1
        N -= 3
        res += 1


print(sugar(N))
