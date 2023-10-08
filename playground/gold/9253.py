# LCS 3

"""
x = abcdefghijklmn
y = bdefg
z = efg

LCS(xi,yj,zk) = efg

LCS(i,j,k) = LCS(xi,yj,zk)
LCS(i,j,k) = LCS(i-1, j-1, k-1) + 1 if xi == yj == zk
LCS(i,j,k) = LCS(i-1, j, k), LCS(i, j-1, k), LCS(i, j, k-1), LCS(i-1, j-1, k), LCS(i-1, j, k-1), LCS(i, j-1, k-1) 중 최댓값 if not (xi == yj == zj)

"""

x = input().strip()
y = input().strip()
z = input().strip()
x = " " + x
y = " " + y
z = " " + z

lcs = [[[0] * len(z) for _ in range(len(y))] for _ in range(len(x))]


for i in range(1, len(x)):
    for j in range(1, len(y)):
        for k in range(1, len(z)):
            if x[i] == y[j] == z[k]:
                lcs[i][j][k] = lcs[i - 1][j - 1][k - 1] + 1
            else:
                lcs[i][j][k] = max(
                    lcs[i - 1][j][k],
                    lcs[i][j - 1][k],
                    lcs[i][j][k - 1],
                    lcs[i - 1][j - 1][k],
                    lcs[i - 1][j][k - 1],
                    lcs[i][j - 1][k - 1],
                )

print(lcs[len(x) - 1][len(y) - 1][len(z) - 1])
