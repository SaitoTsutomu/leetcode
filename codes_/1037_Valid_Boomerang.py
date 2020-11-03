# %% [1037. Valid Boomerang](https://leetcode.com/problems/valid-boomerang/)
# 問題：3点が、全て異なり、直線上にないかどうかを返せ
# 解法：差の比を見る
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        if len(set(tuple(i) for i in points)) != len(points):
            return False
        dx1, dy1 = points[1][0] - points[0][0], points[1][1] - points[0][1]
        dx2, dy2 = points[2][0] - points[1][0], points[2][1] - points[1][1]
        return dx1 * dy2 != dx2 * dy1
