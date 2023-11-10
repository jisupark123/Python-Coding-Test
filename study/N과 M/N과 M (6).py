# 조합 응용

# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.

# - N개의 자연수 중에서 M개를 고른 수열
# - 고른 수열은 오름차순이어야 한다.

N, M = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

tmp = []


def dfs(idx):
    if len(tmp) == M:
        print(*[nums[x] for x in tmp])
        return

    for i in range(idx, N):
        if i not in tmp:
            tmp.append(i)
            dfs(i)
            tmp.pop()


dfs(0)
