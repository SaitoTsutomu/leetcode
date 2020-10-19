# %% [1005. Maximize Sum Of Array After K Negations](https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/)
# 問題：最大となるAの和を返せ。Aの要素はちょうどK回正負を逆にすること
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        i = 0
        while i < len(A) and i < K and A[i] < 0:
            A[i] = -A[i]
            i += 1
        return sum(A) - (K - i) % 2 * min(A) * 2
