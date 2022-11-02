import collections
import re

# 금지된 단어(banned)를 제외한 가장 흔하게 등장하는 단어를 출력하라.

paragraph = "Bob hit a ball, the hit BALL flew after it was hit."
banned = ["hit"]

# 출력 -> ball

# \w -> Word Character (단어 문자), ^ -> not
# 단어 문자가 아닌 것들(".", ",")을 " " 로 변경

words = [
    word
    for word in re.sub(r"[^\w]", " ", paragraph).lower().split()
    if word not in banned
]


# 방법 1

# counts = collections.defaultdict(int)
# for word in words:
#     counts[word] += 1

# print(max(counts, key=counts.get))

# 방법 2

counts = collections.Counter(words)
print(counts.most_common(1)[0][0])  # 1등으로 많이 등장하는 단어
