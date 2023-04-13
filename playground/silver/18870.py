# 좌표 압축

# 이분탐색으로 N과 같은 숫자를 찾는다.
# N보다 더 작은 숫자가 나올 때까지 왼쪽으로 간다.
# 더 작은 숫자가 나오기 전의 인덱스가 압축 값

N = int(input())
X = list(map(int, input().split()))

lst = sorted(set(X))


def find_x(x):
    start = 0
    end = len(lst)
    while start < end:
        mid = (start + end) // 2
        if lst[mid] > x:
            end = mid
        elif lst[mid] < x:
            start = mid
        else:
            return mid


def get_res(i, n):
    while True:
        if i < 0:
            return 0
        if lst[i] == n:
            i -= 1
        else:
            return i + 1


res = []

for x in X:
    res.append(get_res(find_x(x), x))

print(*res)
