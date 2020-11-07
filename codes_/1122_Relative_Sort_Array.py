# %% [1122. Relative Sort Array](https://leetcode.com/problems/relative-sort-array/)
# 問題：arr1を前半と後半に分けて返せ。前半はarr2の順、後半は残りをソートせよ
# 解法：collections.Counterを用いる
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        p = [(i, i in arr2) for i in arr1]
        c1 = collections.Counter(arr2)
        c2 = collections.Counter(i for i, c in p if c)
        return list((c1 | c2).elements()) + sorted(i for i, c in p if not c)
