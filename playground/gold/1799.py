# 비숍


import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

in_range = lambda y, x: 0 <= y < N and 0 <= x < N


def upper_bound(
    diag,
):  # 현재 대각선(우상향) 위치에서부터 끝 대각선까지 뽑힐 가능성이 있는 애들의 갯수 반환
    res = 0
    for d in range(diag, 2 * N - 1):  # 우상향 대각선 모두 탐색
        for y in range(d + 1):
            x = d - y
            # rd[y-x] -> 우하향 대각선에 체스말이 있는지
            if in_range(y, x) and board[y][x] and rd[y - x] == 0:
                res += 1
                break
    return res


def dfs(diag, cnt):  # diag - 우상향 위치, cnt - 놓은 말의 개수
    global ans
    if diag == 2 * N:
        ans = max(ans, cnt)
        return

    if upper_bound(diag) + cnt <= ans:  # 상한값이 ans보다 클 수 없다면
        return

    # 현재 대각선에서 가능한 y,x 조합 찾기
    for y in range(diag + 1):
        x = diag - y
        if in_range(y, x) and board[y][x] and rd[y - x] == 0:
            rd[y - x] = 1
            dfs(diag + 1, cnt + 1)  # 말을 놓기
            rd[y - x] = 0  # 끝나면 말을 다시 빼기

    # 말을 놓지 않는 경우도 탐색
    dfs(diag + 1, cnt)


N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

# 우하향(right down) 대각선
# 중앙 기준으로 쁠마
# (y,x) -> rd[x-y], 왼쪽 아래가 -(n-1), 오른쪽 위가 (n-1)
# 각 좌표의 y,x를 대입하면 몇번째 우하향 자리인지 나온다.
# 각 우하향 대각선에 말이 놓여있는지 기록하는 역할
rd = {x: 0 for x in range(-N + 1, N)}

ans = 0

dfs(0, 0)
print(ans)
