# 거짓말

# N번째 파티에서, 거짓말을 할 수도 안할 수도 있다.
# 만약 해당 파티에 진실을 아는 사람이 하나라도 있다면 진실을 말한다.
# 만약 해당 파티에 진실을 들었던 사람이 있고 거짓을 들었던 사람도 있다면 return
# 만약 해당 파티에 진실을 들었던 사람이 있고 거짓을 들었던 사람이 없다면 진실을 말한다.
# 만약 해당 파티에 진실을 들었던 사람이 없고 거짓을 들었던 사람이 있다면 진실을 말한다.
# 만약 모두가 새로운 사람들이라면 둘 다 진행

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

know = list(map(int, input().split()))
know_people = [] if len(know) == 0 else set(know[1:])
party_people = [list(map(int, input().split()))[1:] for _ in range(M)]

res = 0

heard_true_people = [False for _ in range(N + 1)]
heard_false_people = [False for _ in range(N + 1)]


def dfs(i, cnt_false):
    if i == M - 1:
        global res
        res = max(res, cnt_false)
        return
    is_know_people = False
    for p in party_people[i]:
        if p in know_people:
            is_know_people = True
            break

    if is_know_people:
        for p in party_people[i]:
            heard_true_people[p] = True
        dfs(i + 1, cnt_false)

        return

    is_heard_true_people = False
    is_heard_false_people = False
    for p in party_people[i]:
        if heard_true_people[p]:
            is_heard_true_people = True
        if heard_false_people[p]:
            is_heard_false_people = True
        if is_heard_true_people and is_heard_false_people:
            break


print(know_people)
