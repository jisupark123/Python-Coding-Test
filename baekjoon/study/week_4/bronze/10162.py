# 전자레인지

T = int(input())

A = 5 * 60  # 5분
B = 1 * 60  # 1분
C = 10  # 10초

if T % C != 0:
    print(-1)
    exit()

res = []

for i in (A, B, C):
    cnt = T // i
    T -= cnt * i
    res.append(str(cnt))

print(" ".join(res))
