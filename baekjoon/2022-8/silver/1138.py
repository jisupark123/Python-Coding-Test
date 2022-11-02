# 한 줄로 서기

N = int(input())
info = list(map(int, input().split()))

idx_memo = {}
res = [0] * N


for i, left in enumerate(info):
    j = 0
    while left > 0:
        if res[j] == 0:
            left -= 1
        j += 1

    while res[j] != 0:
        j += 1

    res[j] = i + 1

print(" ".join(map(str, res)))
