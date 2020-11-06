# %% [1047. Remove All Adjacent Duplicates In String](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/)
# 問題：同じ文字が隣り合っていれば削除することを繰り返し、残った文字列を返せ
# 解法：re.subを用いる（線形に処理するより高速）
class Solution:
    def removeDuplicates(self, S: str) -> str:
        T = ""
        while S != T:
            T, S = S, re.sub(r"(.)\1", "", S)
        return S
