# 텀 프로젝트

"""
각 사람마다 순환이 존재하는지 확인
1. 모든 사람을 for문으로 돌면서 함수 f를 실행한다.
2. 함수 f는 순환을 탐지하고 이미 계산했던 사람은 다시 계산되지 않게 저장한다.
- while문을 돈다.
- 순환하는 사람 저장용 set1, 순서 저장용 stack, 결성된 팀 저장용 set2, 결성되지 못한 팀 저장용 set3
- 가리키는 사람을 set1과 stack에 넣고 다음 사람으로 대상을 변경한다. 
- 만약 가리키는 사람이 set2나 set3에 있다면 순환 존재 X, stack에 있는 모두를 set3에 넣는다.
- 만약 가리키는 사람이 set1에 있다면 순환 발생, 가리키는 사람이 나올 때까지 stack에서 꺼내고 set2에 추가한다. 못꺼내고 stack에 남은 사람들은 set3에 추가한다.
"""

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):

    def f(i: int):
        visited = set({i})  # 순환하는 사람 저장용
        stack = [i]  # 순서 저장용
        next_i = graph[i]  # 다음 가리키는 사람
        while True:
            if is_completed(
                next_i
            ):  # 가리키는 사람이 이미 방문처리 되어있다면 순환 존재 X
                for x in stack:
                    solo.add(x)
                return

            if next_i in visited:  # 가리키는 사람이 stack에 있다면 순환 존재 O
                for x in range(len(stack) - 1, -1, -1):
                    team.add(stack[x])
                    if (
                        stack[x] == next_i
                    ):  # 순환이 시작되는 지점 전으로는 모두 팀 결성 X
                        for a in stack[:x]:
                            solo.add(a)
                        return

            visited.add(next_i)
            stack.append(next_i)
            next_i = graph[next_i]

    def is_completed(i):
        return i in team or i in solo

    N = int(input())

    graph = [0] + list(map(int, input().split()))

    team = set()  # 팀이 결성된 사람들
    solo = set()  # 팀이 결성되지 못한 사람들

    for i in range(1, N + 1):
        if not is_completed(i):
            f(i)

    print(len(solo))
