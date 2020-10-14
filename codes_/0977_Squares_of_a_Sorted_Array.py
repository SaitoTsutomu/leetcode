# %% [977. Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)
# 問題：各要素を自乗しソートして返せ
# 解法：両端から絶対値の大きい方を自乗し解に追加していく
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res, i, j = [], 0, len(A) - 1
        while i <= j:
            if abs(A[i]) > abs(A[j]):
                res.append(A[i] ** 2)
                i += 1
            else:
                res.append(A[j] ** 2)
                j -= 1
        return list(reversed(res))
