# 팩토리얼 0의 개수

n = int(input())

num = 1

for i in range(1, n + 1):
    num *= i

num = str(num)
res = 0

for i in range(1, len(num) + 1):
    if num[-i] != "0":
        break
    res += 1

print(res)
