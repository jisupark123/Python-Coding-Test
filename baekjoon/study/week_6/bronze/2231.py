# 분해합

N = int(input())

i = 1

res = 0

while i <= N:
    if i + sum(map(int, list(str(i)))) == N:
        res = i
        break
    i += 1

print(res)
