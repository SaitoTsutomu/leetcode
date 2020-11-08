# %% [1189. *Maximum Number of Balloons](https://leetcode.com/problems/maximum-number-of-balloons/)
# 問題：textから'ballon'を構成できる数を返せ
# 解法：collections.Counterを用いる
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = collections.Counter(text)
        return min(c[s] // n for s, n in collections.Counter("balloon").items())
