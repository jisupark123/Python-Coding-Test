# # 달팽이2

m, n = map(int, input().split())
lst = [[0 for _ in range(n)] for _ in range(m)]
lst[0][0] = 1

# → ↓ ← ↑
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 방향 바뀔 때마다 1씩 올라감
i = 0

# 한걸음에 1씩 올라감
cnt = 1

# 현재 인덱스
curr_idx = (0, 0)

# 리스트를 전부 1로 채울 때까지
while cnt < m * n:

    # 무한 반복(시계 방향)
    curr_direction = direction[i % len(direction)]

    # 앞이 막힐 때까지 무한 반복
    while True:

        # 다음 인덱스
        next_idx = tuple(map(sum, zip(curr_idx, curr_direction)))
        if (
            0 <= next_idx[0] < m
            and 0 <= next_idx[1] < n
            and lst[next_idx[0]][next_idx[1]] == 0
        ):
            lst[next_idx[0]][next_idx[1]] = 1
            cnt += 1
            curr_idx = next_idx
        else:
            break
    i += 1

print(i - 1)
