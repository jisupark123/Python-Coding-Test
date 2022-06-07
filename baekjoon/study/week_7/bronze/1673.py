# 치킨 쿠폰


import sys

for i in sys.stdin.readlines():
    n, k = map(int, i.strip().split())
    t = 0
    r = 0
    while n >= k:
        t = n // k
        r += k * t
        n = n % k + t
    r += n
    print(r)
