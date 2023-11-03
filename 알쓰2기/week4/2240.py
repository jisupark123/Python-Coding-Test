"""
풀이: dfs
자두가 위치한 곳에 자두가 떨어지지 않을 때 분기
현재 먹은 자두 + 남은 턴의 개수가 이전에 구한 최댓값 이하면 분기 종료

-- dfs는 시간초과


풀이: 다이나믹 프로그래밍
s(1)


"""

import sys

input = sys.stdin.readline

T, W = map(int, input().split())

tree_nums = [int(input()) for _ in range(T)]

res = 0

opposite_num = lambda x: 1 if x == 2 else 2


def dfs(turn, move, cnt, num):  # 남은 턴, 남은 이동 횟수, 먹은 자두 개수, 현재 위치(1 or 2)
    if turn == 0:
        global res
        res = max(res, cnt)
        return
    if cnt + turn <= res:
        return

    dfs(turn - 1, move, cnt + 1 if tree_nums[-turn] == num else cnt, num)
    if tree_nums[-turn] != num and move > 0:
        dfs(turn - 1, move - 1, cnt + 1, opposite_num(num))


dfs(T, W, 0, 1)
dfs(T, W - 1, 0, 2)

print(res)
