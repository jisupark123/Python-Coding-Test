# 쉬운 계단 수

"""
n***에서의 경우의 수는 n(n+1)의 경우의 수 + n(n-1)의 경우의 수
몇 자리에서 숫자 몇일 때의 경우의 수를 메모이제이션
가짓수가 2개 이므로 행렬로 표현 n(숫자 자릿수) + 1 X 10(0~9)

"""

import sys

# 재귀 호출 제한 해제
sys.setrecursionlimit(100000000)
n = int(input())

# 몇 자리에서 숫자 몇인지
memo = [[0 for _ in range(10)] for _ in range(n + 1)]
res = 0


def dfs(s, i):
    if memo[i][int(s[-1])]:
        return memo[i][int(s[-1])]
    if len(s) == n:
        print(s)
        return 1
    if s[-1] == "9":
        cnt = dfs(s + "8", i + 1)
        memo[i][int(s[-1])] = cnt
        return cnt
    if s[-1] == "0":
        cnt = dfs(s + "1", i + 1)
        memo[i][int(s[-1])] = cnt
        return cnt
    else:
        cnt = dfs(f"{s}{int(s[-1])+1}", i + 1) + dfs(f"{s}{int(s[-1])-1}", i + 1)
        memo[i][int(s[-1])] = cnt
        return cnt


for i in range(1, 10):
    res += dfs(str(i), 1)

print(res % 1000000000)
