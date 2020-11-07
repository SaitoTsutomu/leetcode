# %% [1128. Number of Equivalent Domino Pairs](https://leetcode.com/problems/number-of-equivalent-domino-pairs/)
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        c = collections.Counter(tuple(sorted(i)) for i in dominoes)
        return sum(n * (n - 1) // 2 for n in c.values())
