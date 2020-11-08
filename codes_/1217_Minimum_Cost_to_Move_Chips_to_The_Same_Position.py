# %% [1217. Minimum Cost to Move Chips to The Same Position](https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/)
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        res = [0, 0]
        for i in position:
            res[i % 2] += 1
        return min(res)
