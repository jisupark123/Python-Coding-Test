# 별찍기

N = int(input())
n = 2 * N - 1
mid = n // 2
up = True
i = 0
while i != -1:
    star = ""
    star += " " * i
    star += "*" * (n - (i * 2))
    star += " " * i
    print(star)
    if i == mid:
        up = False
    i += 1 if up else -1
