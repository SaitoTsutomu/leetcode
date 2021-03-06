# %% [572. *Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)
# 問題：tがsの部分木かどうかを返す
# 解法：再帰を用いる
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode, just=False) -> bool:
        if not s or not t:
            return not s and not t
        if not just and (self.isSubtree(s.left, t) or self.isSubtree(s.right, t)):
            return True
        return s.val == t.val and (
            self.isSubtree(s.left, t.left, True)
            and self.isSubtree(s.right, t.right, True)
        )
