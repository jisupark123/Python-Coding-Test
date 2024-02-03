# 나머지 합

"""
* M으로 뺀 나머지가 같은 수끼리 빼면 M으로 뺀 나머지가 0으로 되는 원리를 이용

1. 배열의 누적합을 생성한다. 이때 각 누적합을 M으로 뺀 나머지를 저장한다. (remain_cnt)
2. result를 선언, 초기값은 나머지가 0인 누적합의 개수다. (remain_cnt[0]) (1개만 골라도 나머지가 0이기 때문에 초기값을 이렇게 정한다.)
3. remain_cnt를 돌면서 2개를 뽑는 경우의 수를 구한다.
-> 2개를 뽑는다는 것은 누적합을 빼서 구간합을 구하는 것을 의미한다.
-> 첫줄의 정리를 이용해서 나머지가 0이 되는 구간의 개수를 찾는다.
"""

import math

N, M = map(int, input().split())

nums = list(map(int, input().split()))
remain_cnt = [0] * M  # M으로 나눈 나머지가 아무리 커도 M을 넘지 못한다.

_sum = 0

for n in nums:
    _sum += n
    remain_cnt[_sum % M] += 1

ans = remain_cnt[0]

for n in remain_cnt:
    ans += math.comb(n, 2)

print(ans)
