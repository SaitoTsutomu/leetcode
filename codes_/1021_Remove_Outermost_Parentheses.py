# %% [1021. Remove Outermost Parentheses](https://leetcode.com/problems/remove-outermost-parentheses/)
# 問題：一番外側の括弧を取り除け
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res, n = "", 0
        for s in S:
            if s == "(":
                if n:
                    res += "("
                n += 1
            else:
                n -= 1
                if n:
                    res += ")"
        return res
