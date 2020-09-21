# %% [917. Reverse Only Letters](https://leetcode.com/problems/reverse-only-letters/)
# 問題：アルファベットだけ逆順にせよ
# 解法：アルファベットのみ反転したジェネレーターを用いる
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        it = reversed([s for s in S if s.isalpha()])
        return "".join(next(it) if s.isalpha() else s for s in S)
