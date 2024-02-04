# 세 수의 합

"""
세수의 합 k의 최대치를 이분 탐색으로 구한다.
k가 주어지면 수행할 연산은 다음과 같다.

1. nums 배열에서 두개의 수를 뽑는다.
2. 뽑은 두 수의 합과 k의 차이의 수가 num_set에 있는지 검사한다. 
-> 검사하려는 수가 뽑은 두 수와 같으면 안된다.
3. num_set에 있으면 가능한 것
"""

import sys

input = sys.stdin.readline


def possible(k):
    if k not in num_set:
        return False

    for a in range(N - 1):
        for b in range(a + 1, N):
            sub = k - (nums[a] + nums[b])
            if sub not in (nums[a], nums[b]):
                return True

    return False


N = int(input())

nums = [int(input()) for _ in range(N)]
num_set = set(nums)

ans = 0

start = 0
end = N

while start <= end:
    mid = (start + end) // 2
    if possible(mid):
        ans = max(ans, mid)
        start = mid + 1
    else:
        end = mid - 1

print(ans)
