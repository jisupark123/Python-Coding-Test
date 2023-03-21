# 랜선 자르기


def test(length: int) -> bool:
    return sum(map(lambda x: x // length, cables)) >= N


K, N = map(int, input().split())
cables = [int(input()) for _ in range(K)]

i = int(sum(cables) / N)
start = 1
end = int(sum(cables) / N)


while start != end:
    middle = (start + end) // 2 + 1
    if test(middle):  # 가능한 길이면 위로
        start = middle
    else:
        end = middle - 1

print(start)
