# n = int(input())
import sys

sys.setrecursionlimit(10**6)
n = int(input())
num_list = ["0"]


def dfs(num):
    num_list.append(num)
    for i in range(int(num[-1]) - 1, -1, -1):
        dfs(num + str(i))


for i in range(1, 10):
    dfs(str(i))

if len(num_list) < n + 1:
    print(-1)
else:
    num_list.sort(key=lambda x: (len(x), x))
    print(num_list[n])
