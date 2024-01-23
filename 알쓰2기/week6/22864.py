# 피로도

A, B, C, M = map(int, input().split())

tired = 0
ans = 0

for _ in range(24):
    if tired + A > M:  # 피로도를 넘기면 휴식
        tired = max(0, tired - C)
    else:
        ans += B
        tired += A

print(ans)
