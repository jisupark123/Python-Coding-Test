# 소인수분해


N = int(input())
i = 2

while N != 1:
    if N % i == 0:
        N = N // i
        print(i)
    else:
        i += 1
