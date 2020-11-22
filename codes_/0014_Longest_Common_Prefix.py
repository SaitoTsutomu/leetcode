# %% [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)
# 問題：全単語に共通する最長のプレフィックスを返せ
# 解法：itertools.zip_longestを用いる
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i, cc in enumerate(itertools.zip_longest(*strs)):
            if not all(cc[0] == c for c in cc[1:]):
                return strs[0][:i]
        return strs[0] if strs else ""
