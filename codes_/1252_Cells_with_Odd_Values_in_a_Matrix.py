# %% [1252. Cells with Odd Values in a Matrix](https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/)
# 問題：indicesの行と列をそれぞれ+1し、奇数の数を返せ
# 解法：NumPyを用いる
import numpy as np


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        a = np.zeros((n, m))
        for i, j in indices:
            a[i, :] += 1
            a[:, j] += 1
        return len(a[a % 2 == 1])
