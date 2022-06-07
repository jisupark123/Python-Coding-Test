# 방 번호

N = input()

cnt = {}

for i in range(10):
    cnt[i] = 0

for n in N:
    cnt[int(n)] += 1


a = abs(cnt[6] - cnt[9])
cnt[-1] = min(cnt[6], cnt[9]) + (a // 2 if a % 2 == 0 else a // 2 + 1)
cnt[6] = 0
cnt[9] = 0

print(max(cnt.values()))
