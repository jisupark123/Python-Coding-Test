# 싸이클

N, P = map(int, input().split())

num = N
nums = []

while True:
    num = (num * N) % P
    try:
        i = nums.index(num)
        print(len(nums) - i)
        break
    except:
        nums.append(num)
