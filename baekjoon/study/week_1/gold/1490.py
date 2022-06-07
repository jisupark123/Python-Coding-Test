# 자리수로 나누기


# def devide_by_cipher():
#     N = int(input())

#     def can_self_devide(num):
#         for n in str(num):
#             if n == "0":
#                 continue
#             if num % int(n) != 0:
#                 return False
#         return True


#     i = 1
#     while True:
#         for j in range(i):
#             if can_self_devide(N + j):
#                 return print(N + j)
#         i *= 10
#         N *= 10


# devide_by_cipher()
def gcd_n(num):
    nums = [int(n) for n in str(num)]

    def gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a

    res = nums[0]
    for i in range(1, len(nums)):
        res = gcd(res, nums[i])

    return res


def devide_by_cipher():
    N = int(input())
    i = 1
    while True:
        for j in range(i):
            gcd = gcd_n(N + j)
            if (N + j) % gcd == 0:
                return print(N + j)
        i *= 10
        N *= 10


# devide_by_cipher()
print(gcd_n(13))
