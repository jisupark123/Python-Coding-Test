# 수들의 합

# S = int(input())

n = int(input())
sum = 0
result = 0
for i in range(1, n + 1):
    sum += i
    result += 1
    if sum > n:
        result -= 1
        break

print(result)


# num = 0
# res = 0
# for n in range(1, S + 1):
#     num += n
#     res += 1
#     if num > S:
#         print(n - 1)
#         print(res - 1)
#         break
