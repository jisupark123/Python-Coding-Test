# Z

N, r, c = map(int, input().split())

num = -1
res = 0


def a(start_row, start_col, n):
    global num
    global res
    if start_row == r and start_col == c:
        res = num + 1
        return
    if n == 1:
        num += 1
        return

    if r < start_row + (n // 2) and c < start_col + (n // 2):  # 왼쪽 위
        num += 0
        a(start_row, start_col, n // 2)
    if r < start_row + (n // 2) and c >= start_col + (n // 2):  # 오른쪽 위
        num += n**2 // 4
        a(start_row, start_col + n // 2, n // 2)
    if r >= start_row + (n // 2) and c < start_col + (n // 2):  # 왼쪽 아래
        num += n**2 // 2
        a(start_row + n // 2, start_col, n // 2)
    if r >= start_row + (n // 2) and c >= start_col + (n // 2):  # 오른쪽 아래
        num += n**2 // 4 * 3
        a(start_row + n // 2, start_col + n // 2, n // 2)


a(0, 0, 2**N)
print(res)
