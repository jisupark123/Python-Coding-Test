# 전화번호 목록

"""
트라이 알고리즘
-> 단어 사전을 트리 형태로 만들어서 탐색

1. 문자를 길이가 긴 순서대로 정렬한다.
2. 트리를 생성한다. 각 키값(0~9)을 빈 리스트로 초기화한다.
2. 트리에 문자를 넣는다. 만약 해당 인덱스에 길이가 1인 빈 리스트가 있다면 빈 리스트 10개로 초기화된 새로운 리스트를 생성한다.
3. 만약 문자의 마지막이고, 트리에 넣으려는 해당 자리에 길이가 10인 리스트가 있다면(이미 해당 문자가 존재한다면) 'NO'를 출력한다.
"""

import sys

input = sys.stdin.readline


def dfs(num, i, l):  # l -> 주소값
    if i == len(num) - 1:
        if len(l[int(num[i])]) == 10:
            return False
        else:
            return True

    if len(l[int(num[i])]) == 0:
        l[int(num[i])] = [[] for _ in range(10)]

    return dfs(num, i + 1, l[int(num[i])])


T = int(input())

for _ in range(T):

    n = int(input())
    nums = [input().strip() for _ in range(n)]
    nums.sort(key=len, reverse=True)

    tree = [[] for _ in range(10)]

    ans = "YES"
    for num in nums:

        if dfs(num, 0, tree) == False:
            ans = "NO"
            break
    print(ans)
