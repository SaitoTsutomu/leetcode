# %% [1051. Height Checker](https://leetcode.com/problems/height-checker/)
# 問題：ソートしたとき異なる要素数を返せ
# 解法：sortedを用いる
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(i != j for i, j in zip(heights, sorted(heights)))
