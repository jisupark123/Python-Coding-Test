# ACM 호텔

T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    y = N % H * 100 if N % H != 0 else H * 100
    x = (N // H) + 1 if N % H != 0 else N // H
    print(y + x)
