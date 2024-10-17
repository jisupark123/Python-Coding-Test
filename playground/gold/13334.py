# 철로

"""
스위핑 알고리즘

- 큐 안의 원소들은 모두 길이가 d인 같은 라인 안에 들어갈 수 있도록 유지한다.
- 원소(시작점, 도착점)가 들어오면 같은 라인에 공존할 수 없는 원소들을 모두 pop 시킨다.
- 따라서 큐 안의 원소들은 시작점을 기준으로, 들어오는 원소들은 도착점을 기준으로 정렬시킨다.
- 큐는 원소가 계속 갱신되므로 우선순위 큐로 정렬을 유지한다.

1. a -> 시작점과 도착점 정보를 도착점 기준으로 오름차순 정렬
2. b -> 우선순위 큐 (시작점을 기준으로 정렬)
3. a에서 원소를 하나씩 빼서 b에 push
3-1. push된 원소의 도착점 - 큐의 첫번째 원소의 시작점 > d 일 경우
-> push된 원소의 도착점 - 시작점 <= d가 될 때까지 pop
4. b의 원소의 개수만큼 결과값 갱신
5. 3~4 반복
"""

import sys
import heapq

input = sys.stdin.readline

n = int(input())
pos = [list(map(int, input().split())) for _ in range(n)]
d = int(input())
pos = [[s, e] if s < e else [e, s] for s, e in pos]
pos = [[s, e] for s, e in pos if e - s <= d]
pos.sort(key=lambda x: x[1])

if len(pos) == 0:
    print(0)
    exit(0)

q = [pos[0][0]]
ans = 1

for start, end in pos[1:]:
    heapq.heappush(q, start)

    if end - q[0] > d:
        for _ in range(len(q) - 1):
            if end - q[0] > d:
                heapq.heappop(q)
            else:
                break

    ans = max(ans, len(q))

print(ans)
