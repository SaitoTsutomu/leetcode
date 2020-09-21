# %% [922. Sort Array By Parity II](https://leetcode.com/problems/sort-array-by-parity-ii/)
# 問題：アルファベットだけ逆順にせよ
# 解法：アルファベットのみ反転したジェネレーターを用いる
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = (a for a in A if a % 2)
        even = (a for a in A if not a % 2)
        return [k for i, j in zip(even, odd) for k in [i, j]]
