# LCS

"""
x = ACAYKP
y = CAPCAK
LCS(xn,ym) = ACAK

LCS(n,m) = LCS(xn,ym)
LCS(n,m) = LCS(n-1, m-1) + 1 if xn == ym
LCS(n,m) = LCS(n, m-1), LCS(n-1, m) 중 최댓값 if xn != ym

LCS(0,0) = 0
"""

x = input().strip()
y = input().strip()


lcs = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]
x = " " + x
y = " " + y

for n in range(1, len(x)):
    for m in range(1, len(y)):
        # n = i if i < len(x) else len(x) - 1
        # m = i if i < len(y) else len(y) - 1
        if x[n] == y[m]:
            lcs[n][m] = lcs[n - 1][m - 1] + 1
        else:
            lcs[n][m] = max(lcs[n - 1][m], lcs[n][m - 1])

print(lcs[len(x) - 1][len(y) - 1])
