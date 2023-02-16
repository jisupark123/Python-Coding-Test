# 피보나치 함수

from sys import stdin

input = stdin.readline

# [0,1] -> 0이 0번, 1이 1번
fibo = [[1, 0], [0, 1]]
for n in range(2, 41):
    zero = fibo[n - 2][0] + fibo[n - 1][0]
    one = fibo[n - 2][1] + fibo[n - 1][1]
    fibo.append([zero, one])


T = int(input())

for _ in range(T):
    n = int(input())
    print(fibo[n][0], fibo[n][1])
