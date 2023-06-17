# 가장 가까운 세 사람의 심리적 거리

"""

모든 사람의 MBTI를 set이나 dictionary로 만들고 
MBTI 16개에서 3개를 뽑는 모든 경우의 수를 돌려서 최소인 심리적인 거리를 구한다.

"""

import sys
from collections import defaultdict

input = sys.stdin.readline


def get_diff_cnt(a: str, b: str):
    cnt = 0
    for i in range(4):
        if a[i] != b[i]:
            cnt += 1

    return cnt


T = int(input())

for _ in range(T):
    N = int(input())
    mbti_dict = defaultdict(int)
    for mbti in input().strip().split(" "):
        mbti_dict[mbti] += 1

    res = 1e9

    for mbti1 in mbti_dict.keys():
        for mbti2 in mbti_dict.keys():
            for mbti3 in mbti_dict.keys():
                key_dict = defaultdict(int)
                for mbti in [mbti1, mbti2, mbti3]:
                    key_dict[mbti] += 1

                flag = True
                for key in [mbti1, mbti2, mbti3]:
                    if key_dict[key] > mbti_dict[key]:
                        flag = False

                if flag:
                    res = min(
                        res,
                        get_diff_cnt(mbti1, mbti2)
                        + get_diff_cnt(mbti2, mbti3)
                        + get_diff_cnt(mbti1, mbti3),
                    )

    print(res)
