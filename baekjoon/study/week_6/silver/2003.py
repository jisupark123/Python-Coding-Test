# 수들의 합 2

N, M = map(int, input().split())  # 수열의 개수 N과 구해야 하는 합 M

sequence = list(map(int, input().split()))  # 수열을 입력 받음
res = 0

for i in range(len(sequence)):  # i는 수열을 순회한다.
    total = 0
    j = i
    while total < M and j < len(sequence):  # j는 i부터 시작해서 목표값 M을 달성하면 res에 1을 추가하고
        total += sequence[j]  # 목표값 M을 초과하면 while문을 중단하고 다음 수(i)로 넘어감
        if total == M:
            res += 1
            break
        j += 1

print(res)
