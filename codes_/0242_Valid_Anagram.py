# %% [242. *Valid Anagram](https://leetcode.com/problems/valid-anagram/)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)
