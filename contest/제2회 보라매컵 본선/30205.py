# 전역 임무

"""
1. 기지에 진입
2. 숫자가 작은 순서대로 정렬한다.
3. -1의 숫자를 저장해놓고 제일 약한 몬스터부터 조진다.
4. 몬스터를 죽일 파워가 부족하다면 -1을 하나 소비한다.
5. 파워가 부족하고 소비할 -1이 없다면 임무 달성 실패
6. 끝까지 올라간다면 기지 파괴 성공 (나가기 전에 가진 아이템을 모두 소진한다)
"""

import sys


input = sys.stdin.readline

N, M, power = map(int, input().split())


bases = [list(map(int, input().split())) for _ in range(N)]

for base in bases:
    base.sort()
    item_cnt = 0
    start_i = 0
    for i in range(len(base)):
        if base[i] == -1:
            item_cnt += 1
        else:
            start_i = i
            break

    i = start_i
    while i < len(base):
        if power >= base[i]:
            power += base[i]
            i += 1
        else:
            if item_cnt > 0:
                power *= 2
                item_cnt -= 1
            else:
                print(0)
                exit(0)

    for _ in range(item_cnt):
        power *= 2

print(1)
