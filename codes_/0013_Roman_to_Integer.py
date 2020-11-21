# %% [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/)
# 問題：ローマ数字から整数を求めよ
# 解法：次の文字より小さければ-1倍する
class Solution:
    def romanToInt(self, s: str) -> int:
        dc = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        return sum(dc[c] * ((dc[c] >= dc[n]) * 2 - 1) for c, n in zip(s, s[1:] + "I"))
