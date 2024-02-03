# 숫자구슬


# 최댓값을 x로 잡았을 때 M번으로 나누는게 가능한지
def possible(x):
    res = []  # 각 그룹을 구성하는 구슬의 개수
    start = 0
    for i in range(M):
        end = split(start, x, M - i)  # M-i -> 남은 횟수

        if end == -1:  # 이미 불가능 (첫 구슬부터 x를 초과)
            return False

        res.append(end - start + 1)
        start = end + 1

    if start != N:
        return False

    return (True, res)


# 시작점(start)부터 합이 x 이하가 되는 최대 인덱스를 구하기
# 남은 횟수(r)을 고려해서 최댓값을 조정
# 시작점부터 x를 초과하면 -1 return
#
def split(start, x, r):
    if beads[start] > x:
        return -1
    s = 0
    for i in range(start, N - r + 1):
        s += beads[i]
        if s > x:
            return i - 1
    return N - r


N, M = map(int, input().split())

beads = list(map(int, input().split()))

start = 0
end = N * 100

ans_num = 1e9
ans_arr = []
while start <= end:
    mid = (start + end) // 2
    res = possible(mid)
    if res == False:
        start = mid + 1
    else:
        end = mid - 1
        if ans_num > mid:
            ans_num = mid
            ans_arr = res[1]


print(ans_num)
print(*ans_arr)
