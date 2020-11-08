# %% [1232. Check If It Is a Straight Line](https://leetcode.com/problems/check-if-it-is-a-straight-line/)
# 問題：同一直線上にあるかどうかを返せ
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0, y0), (x1, y1) = coordinates[:2]
        x10, y10 = x1 - x0, y1 - y0
        return all(x10 * (y - y1) == (x - x1) * y10 for x, y in coordinates[2:])
