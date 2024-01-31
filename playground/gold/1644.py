# 소수의 연속합

N = int(input())

prime_nums = [x for x in range(N + 1)]

# 에라스토 테네스의 체
for i in range(2, int(N**0.5) + 1):
    if prime_nums[i] != 0:
        x = i * 2
        while x <= N:
            prime_nums[x] = 0
            x += i

# 소수
prime_nums = [x for x in prime_nums[2:] if x != 0]

# 누적합
accumulate_sum = prime_nums[:]
for i in range(1, len(accumulate_sum)):
    accumulate_sum[i] += accumulate_sum[i - 1]

"""
1. 누적합 각 원소마다 N과 얼마나 차이나는지 계산한 리스트를 생성한다.
2. 누적합 리스트를 set 자료형으로 만든다. 이 때 0을 포함한다.
3. 1번의 리스트를 돌면서 누적합 리스트에 원소가 포함되어 있는지 검사한다.
4. 포함되어 있는 개수가 정답
"""

sub_lst = list(map(lambda x: x - N, accumulate_sum))

accumulate_sum = set(accumulate_sum)
accumulate_sum.add(0)

ans = 0

for num in sub_lst:
    if num in accumulate_sum:
        ans += 1

print(ans)
