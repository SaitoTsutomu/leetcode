# %% [1200. Minimum Absolute Difference](https://leetcode.com/problems/minimum-absolute-difference/)
# 問題：差が最小となる組を返せ
# 解法：sortを用いる
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mn = min(j - i for i, j in zip(arr, arr[1:]))
        return [[i, j] for i, j in zip(arr, arr[1:]) if j - i == mn]
