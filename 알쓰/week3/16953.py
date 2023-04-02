# A → B

# a - b 길이만큼의 큐를 생성
# 큐의 초기값은 a
#
# 1. 큐에서 숫자 n을 꺼낸다.
# 2. c <- n * 2
#    c가 b보다 작거나 같고 dp[c]가 dp[n] + 1 보다 작으면
#    dp[c] <- dp[n] + 1
#    큐에 c를 추가한다.
# 3. c <- n의 오른쪽에 1 추가
#    c가 b보다 작거나 같고 dp[c]가 dp[n] + 1 보다 작으면
#    dp[c] <- dp[n] + 1
#    큐에 c를 추가한다.
# 4. 큐가 비었으면 dp[b] 출력

# 해결법 1 -> dp롤 메모이제이션 (위의 해결법)
# 해결법 2 -> 메모이제이션 사용 X (아래의 해결법)

# 이 문제는 최대 입력이 10억이지만 2를 곱하는 연산과 1을 붙이는 연산이 수를 빨리 키워주므로
# 메모이제이션 기법을 사용할 필요가 없다.
# 그리고 큐에서 나오는 횟수를 찍어보았을 때 두 해결법(dp를 사용했을 때와 사용하지 않았을 때) 모두 다 74007번으로 같은 걸로 봐서
# 겹치는 연산이 없다는 것을 알 수 있다.
# 따라서 괜히 메모이제이션 기법을 사용했다가 메모리 초과가 나는 문제다.


from collections import deque


a, b = map(int, input().split())

dp = [-1] * (b + 1)
dp[a] = 1
queue = deque([a])

while queue:
    n = queue.popleft()
    next_step = n * 2
    if next_step <= b and dp[next_step] < dp[n] + 1:
        dp[next_step] = dp[n] + 1
        queue.append(next_step)

    next_step = int(f"{n}1")
    if next_step <= b and dp[next_step] < dp[n] + 1:
        dp[next_step] = dp[n] + 1
        queue.append(next_step)

print(dp[b])

########################################################################################


from collections import deque


a, b = map(int, input().split())


queue = deque([(a, 1)])
_min = 1e9

while queue:
    n, cnt = queue.popleft()
    if n == b:
        _min = min(_min, cnt)
    next_step = n * 2
    if next_step <= b:
        queue.append((next_step, cnt + 1))

    next_step = int(f"{n}1")
    if next_step <= b:
        queue.append((next_step, cnt + 1))

print(-1 if _min == 1e9 else _min)
