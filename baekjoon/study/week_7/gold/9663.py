# N-Queen


def check(x):  # 퀸을 놓을 수 있는지 체크하는 함수
    for i in range(x):  # 만약 3행까지 놓여졌다면 1 ~ 3행(x)까지 서로에 대해 검사한다.

        # 같은 열이나 대각선에 놓여질 시 False를 return
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True


def dfs(x):  # 첫 행부터 순회하며 재귀 호출 (x가 행 값이다.)
    global res
    if x == N:  # 중간에 안막히고 끝까지 N개의 퀸을 놓으면 결과값에 1 추가한다.
        res += 1
        return
    for i in range(N):
        row[x] = i
        if check(x):  # 퀸을 놓을 수 있는지 체크하는 함수
            dfs(x + 1)


N = int(input())

res = 0
row = [0] * N  # 체스판의 정보를 담을 배열 (인덱스가 행, 값이 열)

dfs(0)
print(res)
