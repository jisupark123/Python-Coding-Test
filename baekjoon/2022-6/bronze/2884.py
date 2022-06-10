# 알람 시계

H, M = map(int, input().split())

for _ in range(45):
    M -= 1
    if M == -1:
        H -= 1
        M = 59
    if H == -1:
        H = 23

print(H, M)
