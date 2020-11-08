# %% [1207. Unique Number of Occurrences](https://leetcode.com/problems/unique-number-of-occurrences/)
# 問題：同一の頻度がないかを返せ
# 解法：collections.Counterを用いる
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        v = collections.Counter(arr).values()
        return len(v) == len(set(v))
