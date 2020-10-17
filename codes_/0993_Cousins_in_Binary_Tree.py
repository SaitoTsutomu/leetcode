# %% [993. Cousins in Binary Tree](https://leetcode.com/problems/cousins-in-binary-tree/submissions/)
# 問題：xとyが「同じ深さで親が違う」かを返せ
# 解法：深さと親を求める関数を作成
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        dx, px = depth(None, root, 0, x)
        dy, py = depth(None, root, 0, y)
        return dx == dy and px != py


def depth(parent, node, cur, mod):
    if node:
        if node.val == mod:
            return cur, parent
        return depth(node, node.left, cur + 1, mod) or depth(
            node, node.right, cur + 1, mod
        )
