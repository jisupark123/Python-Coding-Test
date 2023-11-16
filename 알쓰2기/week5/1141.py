# 접두사

import sys

input = sys.stdin.readline

N = int(input())

words = [input().strip() for _ in range(N)]
words = list(set(words))  # 중복 제거


def is_prefix(a, b):
    return a in b or b in a


# i,j -> i,j가 접두어 관계이면 1, 아니면 0
table = [[0] * len(words) for _ in range(len(words))]
for i in range(len(words)):
    for j in range(len(words)):
        prefix = is_prefix(words[i], words[j])
        table[i][j] = 1 if prefix else 0


# 크기를 n으로 설정했을 때 가능한 부분 집합이 존재하는지
def possible(n):
    ans = False
    tmp = []

    def dfs(idx):
        nonlocal ans
        if ans:
            return
        if len(tmp) == n:
            ans = True
            return

        for i in range(idx, len(words)):
            p = sum([table[i][j] for j in tmp]) == 0  # 접두어가 이미 tmp에 존재하는지 검사
            if p:
                tmp.append(i)
                dfs(i)
                tmp.pop()

    dfs(0)
    return ans


start = 1
end = len(words)
res = 1

while start <= end:
    mid = (start + end) // 2
    if possible(mid):
        res = max(res, mid)
        start = mid + 1
    else:
        end = mid - 1

print(res)
