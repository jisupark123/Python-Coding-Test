# 스도쿠
#
# 스도쿠를 돌면서 빈자리(-1)를 탐색한다
# 빈자리에 1~9 를 넣어보고 가능하다면 재귀함수를 호출한다.
# 만약 가능한 케이스가 발견되면 즉시 함수를 종료한다.

# 열쇠 -> test 함수에서 순회할 때 빈자리에 뭐가 들어갈 수 있는지 업데이트해서 재검사를 방지한다.

from copy import deepcopy


# row,col에 새로운 값이 들어왔을 때, 가능한지 검사하는 함수
def test(s: list[list[int]], row: int, col: int) -> bool:
    # row 검사
    cnt = 0
    nums = []  # 0이 아닌 모든 수를 저장
    empty = []  # 숫자가 빈자리를 저장
    for i in range(9):
        if s[row][i] == 0:  # 0이면 empty에 넣기
            empty.append((row, i))
        elif i != col:  # 0이 아니고 자기자신도 아니면 nums에 넣기
            nums.append(s[row][i])
        if s[row][i] != s[row][col] and i != col:  # 숫자가 안겹치면
            cnt += 1
    if len(empty) > 0:
        for e in empty:
            # 다시 꺼내서 nums에 있는 모든 수를 제외하고 저장
            poss_value[e] = [x for x in poss_value[e] if x not in nums]
    if cnt != 8:
        return False

    # col 검사
    cnt = 0
    nums = []  # 0이 아닌 모든 수를 저장
    empty = []  # 숫자가 빈자리를 저장
    for i in range(9):
        if s[i][col] == 0:
            empty.append((i, col))
        elif i != row:
            nums.append(s[i][col])
        if s[i][col] != s[row][col] and i != row:
            cnt += 1
    if len(empty) > 0:
        for e in empty:
            # 다시 꺼내서 nums에 있는 모든 수를 제외하고 저장
            poss_value[e] = [x for x in poss_value[e] if x not in nums]
    if cnt != 8:
        return False

    # 칸 검사

    sections = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    row_section = []  # 칸에 해당하는 행들
    col_section = []  # 칸에 해당하는 열들
    for section in sections:
        if row in section:
            row_section = section
            break
    for section in sections:
        if col in section:
            col_section = section
            break

    cnt = 0
    nums = []  # 0이 아닌 모든 수를 저장
    empty = []  # 숫자가 빈자리를 저장

    for r in row_section:
        for c in col_section:
            if s[r][c] == 0:
                empty.append((r, c))
            elif (r, c) != (row, col):
                nums.append(s[r][c])
            if s[r][c] != s[row][col] and (r, c) != (row, col):
                cnt += 1
    if len(empty) > 0:
        for e in empty:
            # 다시 꺼내서 nums에 있는 모든 수를 제외하고 저장
            poss_value[e] = [x for x in poss_value[e] if x not in nums]
    if cnt != 8:
        return False

    return True  # 다 통과하면 가능


sudoku = [list(map(int, input().split())) for _ in range(9)]  # 스도쿠 판
empty_place: list[tuple[int, int]] = []  # 빈자리 [(row,col)]
for row in range(9):
    for col in range(9):
        if sudoku[row][col] == 0:
            empty_place.append((row, col))

poss_value = {}  # 각 빈자리마다 들어갈 수 있는 값을 관리하는 딕셔너리 (초기값은 1~9)
for e in empty_place:
    poss_value[e] = list(range(1, 10))
res = [[]]


def dfs(s: list[list[int]], empty_place: list[tuple[int, int]]):
    if len(empty_place) == 0:
        global res
        res = s
        return True
    for i in range(len(empty_place)):
        row = empty_place[i][0]
        col = empty_place[i][1]
        for num in poss_value[empty_place[i]]:
            new_sudoku = deepcopy(s)
            new_sudoku[row][col] = num
            new_empty_place = deepcopy(empty_place)
            del new_empty_place[i]
            if test(new_sudoku, row, col):  # 그곳에 num을 넣어도 괜찮은가?
                flag = dfs(new_sudoku, new_empty_place)
                if flag == True:
                    return True


print()
dfs(sudoku, empty_place)
# for r in res:
#     for c in r:
#         print(c, end=" ")
#     print()

# for p in poss_value.keys():
#     print(p, poss_value[p])

result = [
    [1, 3, 5, 4, 6, 9, 2, 7, 8],
    [7, 8, 2, 1, 3, 5, 6, 4, 9],
    [4, 6, 9, 2, 7, 8, 1, 3, 5],
    [3, 2, 1, 5, 4, 6, 8, 9, 7],
    [8, 7, 4, 9, 1, 3, 5, 2, 6],
    [5, 9, 6, 8, 2, 7, 4, 1, 3],
    [9, 1, 7, 6, 5, 2, 3, 8, 4],
    [6, 4, 3, 7, 8, 1, 9, 5, 2],
    [2, 5, 8, 3, 9, 4, 7, 6, 1],
]

print(res == result)
