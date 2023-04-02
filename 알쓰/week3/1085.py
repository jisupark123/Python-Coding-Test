# 직사각형에서 탈출


x, y, w, h = map(int, input().split())

x = min(x, abs(x - w))
y = min(y, abs(y - h))
print(min(x, y))
