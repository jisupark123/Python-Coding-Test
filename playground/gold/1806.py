# 부분합


# a에서 b까지의 구간합
def part_sum(a, b):
    if a == 0:
        return accumulate_sum[b]
    return accumulate_sum[b] - accumulate_sum[a - 1]


# S이상을 만족하는 길이 n의 부분합이 있는지
def possible(n):
    for i in range(N - n + 1):
        if part_sum(i, i + n - 1) >= S:
            return True
    return False


N, S = map(int, input().split())

sequence = list(map(int, input().split()))

accumulate_sum = sequence[:]
for i in range(1, N):
    accumulate_sum[i] += accumulate_sum[i - 1]

start = 1
end = N


ans = float("inf")

while start <= end:
    mid = (start + end) // 2
    if possible(mid):
        ans = min(ans, mid)
        end = mid - 1
    else:
        start = mid + 1

print(0 if ans == float("inf") else ans)
