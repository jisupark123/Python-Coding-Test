# 하노이 탑 이동 순서

from sys import maxsize, setrecursionlimit
from itertools import permutations
from copy import deepcopy


# 원판 옮기기
# 만약 바로 이전의 상태로 되돌아간다면 오류
def move(plates: list[list[int]], prev_to: int, _from: int, to: int) -> list[list[int]]:
    if prev_to == (_from):
        raise PermissionError("한 턴 전에 옮긴 원판은 다시 옮길 수 없음")

    if len(plates[_from]) == 0:
        raise IndexError(f"원판 {_from}: 옮길 원판이 없음")

    if len(plates[to]) != 0 and plates[to][-1] < plates[_from][-1]:
        raise PermissionError("쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.")
    else:
        plates[to].append(plates[_from].pop())
        return plates


def is_finished(plates: list[list[int]]) -> bool:
    return plates[-1] == list(range(len(plates) - 1, -1, -1))


def dfs(cnt: int, plates: list[list[int]], prev_to: int):

    if is_finished(plates):
        global min_cnt
        min_cnt = min(min_cnt, cnt)
        return

    for _from, to in permutations(range(0, len(plates)), 2):
        try:
            new_plates = move(deepcopy(plates), prev_to, _from, to)
            dfs(cnt + 1, new_plates, to)

        except:
            continue


# 하노이 클래스 복제해야 됨
N = int(input())
min_cnt = maxsize
setrecursionlimit(10000000)
dfs(0, [list(range(N - 1, -1, -1)), [], []], -1)
print(min_cnt)
