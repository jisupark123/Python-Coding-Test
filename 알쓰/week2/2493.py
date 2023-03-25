# 탑

# 스택을 이용한 풀이
# 리스트에 모든 값을 가지고 있으면 요소 하나 당 모든 리스트를 순회해야 하므로 O(N**2)의 시간이 소요된다.
# 따라서 쓸모없는 값을 없애주면서 리스트를 관리한다.
# 쓸모없는 값 -> 큰 수 왼쪽에 있는 작은 수
# 리스트에 들어가는 값 -> (숫자,인덱스 정보)
#
# 1. 요소를 리스트의 마지막 값(x)과 비교한다.
# 2. 요소가 x보다 작다면 push & 결과값 기록(x의 인덱스)
# 3. 요소가 x보다 크거나 같다면 x 삭제(pop)
# 4. 다시 1번 수행

N = int(input())
tops = [int(x) for x in input().split()]

stack = []
res = []
for i in range(N):
    while True:
        if len(stack) == 0:
            res.append(0)
            stack.append((tops[i], i + 1))
            break
        if stack[-1][0] > tops[i]:
            res.append(stack[-1][1])
            stack.append((tops[i], i + 1))
            break
        else:
            stack.pop()
            continue

print(*res)
