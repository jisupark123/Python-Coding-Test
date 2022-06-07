# 오븐 시계

H, M = map(int, input().split())
M += int(input())

H += M // 60
H %= 24
M %= 60

print(H, M)
