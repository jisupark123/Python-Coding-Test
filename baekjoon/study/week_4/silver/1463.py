# 1로 만들기

# 다이나믹 프로그래밍
# 위에서부터 계산하는 방식이 아닌 아래서부터 메모하면서 올라가는 상향식

N = int(input())

memo = [0] * (N + 1)  # 단계를 올라가면서 1까지 가는 경로의 최솟값을 저장

for i in range(2, N + 1):
    # 먼저 N-1을 계산
    memo[i] = memo[i - 1] + 1
    # 예를 들어 i=9면 8+1로 가는게 빠른지 3*3으로 가는게 빠른지 계산
    if i % 3 == 0:
        memo[i] = min(memo[i], memo[i // 3] + 1)
    if i % 2 == 0:
        memo[i] = min(memo[i], memo[i // 2] + 1)
print(memo[N])


# min_cnt = 1e9


# def dfs(count, total):
#     global min_cnt
#     if total == 1:
#         min_cnt = min(min_cnt, count)
#         return
#     if total % 3 == 0:
#         dfs(count + 1, total // 3)
#     if total % 2 == 0:
#         dfs(count + 1, total // 2)
#     dfs(count + 1, total - 1)


# dfs(0, N)
# print(min_cnt)
