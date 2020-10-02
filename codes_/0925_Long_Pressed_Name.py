# %% [925. Long Pressed Name](https://leetcode.com/problems/long-pressed-name/)
# 問題：nameの各文字を1回以上タイプしてtypedになるかを返せ
# 解法：2つの添字を用いる
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        c = lambda s, i, n: s[i] if i < n else ""
        i, j, ni, nj = 0, 0, len(name), len(typed)
        while i < ni or j < nj:
            if c(name, i, ni) != c(typed, j, nj):
                return False
            s = c(name, i + 1, ni)
            while j + 1 < nj and typed[j + 1] != s and typed[j + 1] == typed[j]:
                j += 1
            i, j = i + 1, j + 1
        return True
