# 덩치
import sys


def is_bigger(a: tuple, b: tuple) -> bool:
    if a[0] > b[0] and a[1] > b[1]:
        return True
    else:
        return False


input = sys.stdin.readline
N = int(input())
group = [tuple(map(int, input().split())) for _ in range(N)]
# res = ""

for a in group:
    cnt = 1
    for b in group:
        if is_bigger(b, a):
            cnt += 1
    # res += str(cnt)
    print(cnt, end=" ")
# print(" ".join(res))
