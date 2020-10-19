# %% [1002. Find Common Characters](https://leetcode.com/problems/find-common-characters/)
# 問題：各単語に共通する文字を重複を許して返せ
# 解法：collections.Counterを用いる
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        cc = map(collections.Counter, A)
        return list(functools.reduce(operator.and_, cc).elements())
