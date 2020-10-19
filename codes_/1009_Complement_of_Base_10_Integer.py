# %% [1009. Complement of Base 10 Integer](https://leetcode.com/problems/complement-of-base-10-integer/submissions/)
# 問題：「2進数にし01を交代した数」を10進数にして返せ
# 解法：binを用いる
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return int("".join("01"[c == "0"] for c in bin(N)[2:]), 2)
