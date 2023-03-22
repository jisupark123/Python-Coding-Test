# Yangjojang of The Year

import sys

input = sys.stdin.readline

for _ in range(int(input())):
    print(
        sorted(
            [input().strip().split(" ") for _ in range(int(input()))],
            key=lambda x: int(x[1]),
            reverse=True,
        )[0][0]
    )
