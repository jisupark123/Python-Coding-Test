import sys
from collections import deque

input = sys.stdin.readline


N, M = map(int, input().split())

# 진실을 아는 사람들
true_people = list(map(lambda x: int(x) - 1, input().strip().split()))[1:]

# 사람별로 참가한 파티
people_party = [[] for _ in range(N)]

# 파티별로 참가한 사람
party_people = []

for i in range(M):
    people = list(map(lambda x: int(x) - 1, input().split()))[1:]
    for p in people:
        people_party[p].append(i)
    party_people.append(people)


queue = deque()  # 진실을 아는 사람들
for i in true_people:
    queue.append(i)


res = [1] * M  # 거짓말해도 되는 파티
while queue:
    p = queue.popleft()
    for i in people_party[p]:  # i -> party
        if res[i]:
            res[i] = 0
            for j in party_people[i]:
                queue.append(j)

print(len(list(filter(lambda x: x == 1, res))))
