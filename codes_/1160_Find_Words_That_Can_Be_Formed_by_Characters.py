# %% [1160. Find Words That Can Be Formed by Characters](https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/)
# 問題：charsで構成できる単語の文字数の和を返せ
# 解法：collections.Counterを用いる
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cs = collections.Counter(chars)
        return sum(len(word) for word in words if not collections.Counter(word) - cs)
