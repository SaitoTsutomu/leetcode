# %% [1078. Occurrences After Bigram](https://leetcode.com/problems/occurrences-after-bigram/)
# 問題：firstとsecondに続く単語をすべて返せ
# 解法：re.findallを用いる（単語境界と肯定的後読み）
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        return re.findall(rf"(?<=\b{first} {second}) (\w+)", text)
