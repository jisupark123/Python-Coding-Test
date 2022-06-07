# 개미

# (w * h 격자)
w, h = map(int, input().split())

# 처음 개미의 위치 (p,q)
p, q = map(int, input().split())

# 개미가 움직인 시간
t = int(input())

# 개미가 이동한 거리 - 왕복한 거리
a = (p + t) // w
b = (q + t) // h

if a % 2 == 0:
    x = (p + t) % w
else:
    x = w - (p + t) % w

if b % 2 == 0:
    y = (q + t) % h
else:
    y = h - (q + t) % h

print(x, y)
