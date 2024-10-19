# 수상 택시

"""
순방향의 이동은 어차피 가는 길이기 때문에 역방향의 이동만 고려
이동이 겹치는지 판별

a -> 역방향의 이동들 [[출발, 도착]]
a를 도착지 순으로 오름차순 정렬 

min_e -> 도착지 중 가장 작은 값을 저장
max_s -> 출발지 중 가장 큰 값을 저장
ans -> 총 이동 거리

a의 모든 원소에 대해 다음을 수행
s, e -> 출발, 도착

1. e가 max_s보다 작으면 min_e = min(min_e, e)
2. e가 i보다 크거나 같으면 ans += (i-min_e)*2 (한번 찍고 옴), min_e=e
3. s가 max_s보다 클 때만 ans += s-max_s (s로 이동)
4. max_s 갱신 (s로 이동)

"""


import sys

input = sys.stdin.readline

N, M = map(int, input().split())

moves = [list(map(int, input().split())) for _ in range(N)]
moves = [[a, b] for a, b in moves if a > b]
if len(moves) == 0:
    print(M)
    exit(0)

moves.sort(key=lambda x: x[1])

max_s, min_e = moves[0]
ans = max_s
for s, e in moves[1:]:
    if e < max_s:
        min_e = min(min_e, e)
    else:
        ans += (max_s - min_e) * 2
        min_e = e

    if s > max_s:
        ans += s - max_s
    max_s = max(max_s, s)

ans += (max_s - min_e) * 2
print(ans + (M - max_s))
