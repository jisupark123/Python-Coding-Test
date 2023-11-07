# 기타 레슨

n, m = map(int, input().split())
lst = list(map(int, input().split()))


start = 0
end = sum(lst)
mid = (start + end) // 2

res = end


# n -> 녹화 가능한 길이
def possible(n):
    tmp = 0
    blue_ray_cnt = 1
    for num in lst:
        if num > n:
            return False
        if tmp + num > n:
            tmp = num
            blue_ray_cnt += 1
            if blue_ray_cnt > m:
                return False
        else:
            tmp += num
    return True


while start <= end:
    mid = (start + end) // 2
    if possible(mid):
        res = min(res, mid)
        end = mid - 1
    else:
        start = mid + 1

print(res)
