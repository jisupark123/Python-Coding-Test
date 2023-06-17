# 리모컨


target = int(input())
res = abs(100 - target)

M = int(input())
if M == 0:
    broken = set()
else:
    broken = set(input().strip().split())

for num in range(1000001):
    for n in str(num):
        if n in broken:
            break
    else:
        res = min(res, len(str(num)) + abs(num - target))

print(res)
