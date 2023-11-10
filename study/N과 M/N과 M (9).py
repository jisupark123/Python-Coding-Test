# 순열 응용

# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. \
# N개의 자연수는 서로 같을 수 있다.

# N개의 자연수 중에서 M개를 고른 수열

N, M = map(int, input().split())

nums = list(map(int, input().split()))

tmp = []
s = set()


def dfs():
    if len(tmp) == M:
        s.add(tuple([nums[x] for x in tmp]))
        return
    for i in range(N):
        if i not in tmp:
            tmp.append(i)
            dfs()
            tmp.pop()


dfs()

for n in sorted(list(s)):
    print(*n)
