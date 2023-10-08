# LCS 2

"""
x = ACAYKP
y = CAPCAK
LCS(xn,ym) = ACAK

LCS(n,m) = LCS(xn,ym)
LCS(n,m) = LCS(n-1, m-1) + 1 if xn == ym
LCS(n,m) = LCS(n, m-1), LCS(n-1, m) 중 최댓값 if xn != ym

[0, 0, 0, 0, 0, 0, 0]
[0, 0, 1, 1, 1, 1, 1]
[0, 1, 1, 1, 2, 2, 2]
[0, 1, 2, 2, 2, 3, 3]
[0, 1, 2, 2, 2, 3, 3]
[0, 1, 2, 2, 2, 3, 4]
[0, 1, 2, 3, 3, 3, 4]

dp에서 만든 테이블을 다시 역추적한다.
[-1][-1]에서 시작해서 숫자가 같으면 그쪽으로 가고,
다르면 대각선으로 이동한다. 이 때는 문자열에 추가한다.

"""

x = input().strip()
y = input().strip()

x = " " + x
y = " " + y
lcs = [[0] * (len(y)) for _ in range(len(x))]


for n in range(1, len(x)):
    for m in range(1, len(y)):
        if x[n] == y[m]:
            lcs[n][m] = lcs[n - 1][m - 1] + 1
        else:
            lcs[n][m] = max(lcs[n - 1][m], lcs[n][m - 1])


if lcs[len(x) - 1][len(y) - 1] == 0:
    print(lcs[len(x) - 1][len(y) - 1])
else:
    print(lcs[len(x) - 1][len(y) - 1])
    s = ""
    i = len(x) - 1
    j = len(y) - 1
    while len(s) != lcs[len(x) - 1][len(y) - 1]:
        if lcs[i][j] == lcs[i - 1][j]:
            i -= 1
        elif lcs[i][j] == lcs[i][j - 1]:
            j -= 1
        else:
            s += x[i]
            i -= 1
            j -= 1

    print(s[::-1])
