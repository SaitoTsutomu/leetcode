# %% [999. Available Captures for Rook](https://leetcode.com/problems/available-captures-for-rook/)
# 問題：ルークが取れるポーンの個数を返せ
# 解法：np.argwhereでルークの位置
import numpy as np


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        board = np.array(board)
        x, y = np.argwhere(board == "R")[0]
        return sum(
            bool(re.match(r"R\.*p", "".join(a)))
            for d in [1, -1]
            for a in [board[x, y::d], board.T[y, x::d]]
        )
