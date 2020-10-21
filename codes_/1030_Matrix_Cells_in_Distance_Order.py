# %% [1030. Matrix Cells in Distance Order](https://leetcode.com/problems/matrix-cells-in-distance-order/)
# 問題：[r0, c0]までのマンハッタン距離の短い順に座標を返せ
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        a = [(abs(i - r0) + abs(j - c0), i, j) for i in range(R) for j in range(C)]
        return [i[1:] for i in sorted(a)]
