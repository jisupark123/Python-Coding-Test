# 같이 눈사람 만들래?

"""
숫자 2개 뽑고 나머지는 Two-Pointer로 뽑기

시간복잡도는 N^3 
"""


N = int(input())
nums = list(map(int, input().split()))
nums.sort()
ans = float("inf")

for i in range(N - 3):
    for j in range(i + 3, N):
        a = nums[i] + nums[j]
        start, end = i + 1, j - 1

        while start < end:
            b = nums[start] + nums[end]
            diff = abs(a - b)

            ans = min(ans, diff)

            if a > b:
                start += 1
            else:
                end -= 1


print(ans)
