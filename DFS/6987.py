# 월드컵

T = []
for _ in range(4):
    _input = input().strip()
    scores = _input.split(" ")
    sliced_list = [scores[i : i + 3] for i in range(0, len(scores), 3)]

    T.append(sliced_list)


def solution(res: list[list[int]]) -> bool:
    match = [[-1 for _ in range(6)] for _ in range(6)]  # 6x6 대진표
    while True:
        # 일단 대진표 넣어보고
        # 막히면 DFS 돌리기
        changed = False
        for i in range(6):  # A팀부터 F팀까지의 결과를 순회
            if sum(res[i]) != match[i].count(-1):  # 개수가 맞지 않다면
                return False
            for count in range(3):  # 승->0 무->1 패->2
                if res[i][count] == match[i].count(-1):  # ex 승5, 빈자리5 라면 승으로 채움
                    for j in match[i]:
                        if match[i][j] == -1:
                            match[i][j] = count
                    changed = True
        if not changed:  # 바뀌지 않았다면 dfs 돌림
            dfs()


for test in T:
    print(1 if solution(test) else 0, end=" ")
