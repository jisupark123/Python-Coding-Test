# 순열 직접 구현

from itertools import permutations


# n개 중에 r개를 뽑는 경우
def p(n, r):
    tmp = []
    res = []

    def dfs():
        if len(tmp) == r:
            res.append(tuple(tmp))

        for i in range(n):
            if i not in tmp:
                tmp.append(i)
                dfs()
                tmp.pop()

    dfs()
    return res


a = list(permutations(range(3), 3))
b = p(3, 3)
print(a)
print(b)
