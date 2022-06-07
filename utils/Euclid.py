# 유클리드 호제법 - a, b 의 최대공약수는 b와 a%b의 최대공약수와 같다
# tip - a, b의 최소공배수는 a * b / (a, b의 최대공약수)

# 두수의 최대공약수
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


# 여러수의 최대공약수 (리스트로 매개변수 받음)
def gcd_n(nums):
    def gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a

    res = nums[0]
    for i in range(1, len(nums)):
        res = gcd(res, nums[i])

    return res
