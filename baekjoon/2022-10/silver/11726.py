# 2×n 타일링

# 재귀적으로 푸는 방법
# 2xn의 타일을 채우는 방법의 수 -> 2x(n-1) + 2x(n-2)


def tile(n):
    if n <= 1:
        return 1
    return tile(n - 1) + tile(n - 2)


n = int(input())


lst = [0, 1, 2]

for i in range(3, n + 1):
    lst.append(lst[-1] + lst[-2])

print(lst[n] % 10007)
