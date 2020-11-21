# %% [1237. Find Positive Integer Solution for a Given Equation](https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/)
# 問題：customfunction.f(x, y)は、x, y(> 0)で狭義の単調増加。ustomfunction.f(x, y) == zとなる[x, y]をすべて返せ
# 解法：しらみつぶし
class Solution:
    def findSolution(self, customfunction: "CustomFunction", z: int) -> List[List[int]]:
        res, up = [], z
        for x in range(1, z + 1):
            if customfunction.f(x, 1) > z:
                break
            for y in range(up, 0, -1):
                if customfunction.f(x, y) == z:
                    res.append([x, y])
                    up = y - 1
                    break
        return res
