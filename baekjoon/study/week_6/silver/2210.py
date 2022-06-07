# 숫자판 점프


def dfs(idx, depth, total):
    global res
    if depth == 6:
        res.append(total)
        return

    try:
        dfs(
            tuple(map(lambda x: sum(x), zip(idx, direction[0]))),
            depth + 1,
            total + res[idx[0]][idx[1]],
        )
        dfs(
            tuple(map(lambda x: sum(x), zip(idx, direction[1]))),
            depth + 1,
            total + res[idx[0]][idx[1]],
        )
        dfs(
            tuple(map(lambda x: sum(x), zip(idx, direction[2]))),
            depth + 1,
            total + res[idx[0]][idx[1]],
        )
        dfs(
            tuple(map(lambda x: sum(x), zip(idx, direction[3]))),
            depth + 1,
            total + res[idx[0]][idx[1]],
        )
    except:
        return


keypad = [list(input().split()) for _ in range(5)]

direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]

res = []

for i in range(5):
    for j in range(5):
        dfs((i, j), 0, "")

print(len(res))
