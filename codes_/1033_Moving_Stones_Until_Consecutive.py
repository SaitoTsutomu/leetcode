# %% [1033. Moving Stones Until Consecutive](https://leetcode.com/problems/moving-stones-until-consecutive/)
# 問題：a, b, cの最小または最大を(最小, 最大)の範囲で他の数字とかぶらずに動かせ。[最小回数, 最大回数]を返せ
# 解法：ソートする
class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        x, y, z = sorted([a, b, c])
        mn, mx = 0, z - x - 2
        if mx:
            mn = (y - x > 2 and z - y > 2) + 1
        return [mn, mx]
