# 최대공약수와 최소공배수


a, b = map(int, input().split())

# 최대공약수
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


# 최소공배수
def lcm(a, b):
    return a * b // gcd(a, b)


print(gcd(a, b))
print(lcm(a, b))
