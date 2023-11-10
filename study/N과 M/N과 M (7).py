# 중복 순열 응용

# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.

# - N개의 자연수 중에서 M개를 고른 수열
# - 같은 수를 여러 번 골라도 된다.

N, M = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

tmp = []


def dfs():
    if len(tmp) == M:
        print(*[nums[x] for x in tmp])
        return

    for i in range(N):
        tmp.append(i)
        dfs()
        tmp.pop()


dfs()
