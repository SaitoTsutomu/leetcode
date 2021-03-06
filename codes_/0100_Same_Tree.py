# %% [100. *Same Tree](https://leetcode.com/problems/same-tree/)
# 問題：2つのTreeNodeが同じかどうか調べる
# 解法：再帰的に調べる
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p or not q:
            return p is q
        return (
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )
