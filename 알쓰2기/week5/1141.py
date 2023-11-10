# 접두사

import sys

input = sys.stdin.readline

N = int(input())

words = [input().strip() for _ in range(N)]


# n개의 부분집합으로 묶었을 때 가능한 집합이 나오는지
def possible(n):
    visited = [0] * n

    def dfs(i, depth):
        if depth == n:
            s = [words[idx] for idx in range(n) if not visited[idx]]
            print(depth, s)
            for a in range(len(s) - 1):
                for b in range(a + 1, len(s)):
                    if words[a] in words[b] or words[b] in words[a]:
                        return False
            return True

        for j in range(i, n):
            if not visited[j]:
                visited[j] = 1
                tmp = dfs(j + 1, depth + 1)
                visited[j] = 0
                return tmp

    return dfs(0, 0)


print(possible(4))
