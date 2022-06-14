# 이분탐색


def x_in_list(x, lst):
    start = 0
    end = len(lst) - 1
    mid = (start + end) // 2
    while start <= end:
        if lst[mid] == x:
            return True
        elif lst[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
        mid = (start + end) // 2

    return False
