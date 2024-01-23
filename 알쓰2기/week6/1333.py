# 부재중 전화

N, L, D = map(int, input().split())

ans = (L * N) + (5 * (N - 1))
belling = True  # 전화벨 울리고 있는지
sounding = True  # 노래 나오고 있는지

time = 0

for _ in range(N):
    if belling and not sounding:
        ans = time
        break
    time += 1


print(ans)
