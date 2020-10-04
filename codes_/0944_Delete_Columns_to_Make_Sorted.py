# %% [944. Delete Columns to Make Sorted](https://leetcode.com/problems/delete-columns-to-make-sorted/)
class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        return sum(any(i > j for i, j in zip(t, t[1:])) for t in zip(*A))
