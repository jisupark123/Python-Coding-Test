# 문자열 배열을 받아 애너그램 단위로 그룹핑하라

import collections


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

# 정렬해서 딕셔너리에 집어넣는다.

anagrams = collections.defaultdict(list)

for word in strs:
    anagrams["".join(sorted(word))].append(word)

print(anagrams.values())
