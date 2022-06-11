# 숫자의 개수

A = int(input())
B = int(input())
C = int(input())

res = str(A * B * C)

for n in range(10):
    print(res.count(str(n)))
