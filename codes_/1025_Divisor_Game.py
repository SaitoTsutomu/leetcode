# %% [1025. Divisor Game](https://leetcode.com/problems/divisor-game/)
class Solution:
    def divisorGame(self, N: int) -> bool:
        return not N % 2
