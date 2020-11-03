# %% [1042. Flower Planting With No Adjacent](https://leetcode.com/problems/flower-planting-with-no-adjacent/)
# 問題：n個の庭に4種の花を植えよ。pathsの各要素の2つの庭の花は別にせよ
# 解法：四色問題を解く
class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        res = [0] * n
        dj = [[] for _ in range(n)]
        for i, j in paths:
            dj[max(i, j) - 1].append(min(i, j) - 1)
        for i in range(n):
            res[i] = ({1, 2, 3, 4} - {res[j] for j in dj[i]}).pop()
        return res
