# 흙길 보수하기


import sys

input = sys.stdin.readline


N, L = map(int, input().split())
pool = [list(map(int, input().split())) for _ in range(N)]
pool = [[a, b] if a <= b else [b, a] for a, b in pool]
pool.sort()
ans = 0
last_board = -1
for i in range(N):
    s, e = pool[i]
    if last_board >= s:
        s = last_board + 1

    if s < e:
        r = (e - s) % L
        ans += (e - s) // L + int(bool(r))
        last_board = 0 if r == 0 else e + L - r - 1

print(ans)
