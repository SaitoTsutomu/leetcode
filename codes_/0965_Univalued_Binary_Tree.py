# %% [965. Univalued Binary Tree](https://leetcode.com/problems/univalued-binary-tree/)
# 問題：全valが等しいかを返せ
# 解法：深さ優先探索
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        return dfs(root.left, root.val) and dfs(root.right, root.val)


def dfs(tn, v):
    return not tn or tn.val == v and dfs(tn.left, v) and dfs(tn.right, v)
