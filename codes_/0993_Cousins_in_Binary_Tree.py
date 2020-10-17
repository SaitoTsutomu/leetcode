# %% [993. Cousins in Binary Tree](https://leetcode.com/problems/cousins-in-binary-tree/submissions/)
# 問題：xとyが「同じ深さで親が違う」かを返せ
# 解法：深さと親を求める関数を作成
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        dx, px = depth(None, root, 0, x)
        dy, py = depth(None, root, 0, y)
        return dx == dy and px != py


def depth(parent, tn, cur, val):
    if tn:
        if tn.val == val:
            return cur, parent
        return depth(tn, tn.left, cur + 1, val) or depth(tn, tn.right, cur + 1, val)
