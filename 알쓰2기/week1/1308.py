def days_in_month(year: int, month: int) -> int:
    if month != 2:
        return days[month - 1]
    if year % 400 == 0:
        return 29
    if year % 100 == 0:
        return 28
    if year % 4 == 0:
        return 29
    return 28


a = list(map(int, input().strip().split(" ")))
b = list(map(int, input().strip().split(" ")))

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

res = 0


if b[0] - a[0] >= 1000 and (b[1] > a[1] or (b[1] == a[1] and b[2] >= a[2])):
    print("gg")
    exit(0)


while a[0] != b[0] or a[1] != b[1] or a[2] != b[2]:
    if a[0] == b[0] and a[1] == b[1]:
        res += b[2] - a[2]
        break
    day_cnt = days_in_month(a[0], a[1])
    res += day_cnt - a[2] + 1
    a[0] = a[0] if a[1] != 12 else a[0] + 1
    a[1] = a[1] + 1 if a[1] != 12 else 1
    a[2] = 1

print(f"D-{res}")
