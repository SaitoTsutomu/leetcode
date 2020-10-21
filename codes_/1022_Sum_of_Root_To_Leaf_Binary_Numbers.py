# %% [1022. Sum of Root To Leaf Binary Numbers](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/)
# 問題：葉までのパスを2進数とみなして総和を返せ
# 解法：深さ優先探索
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        return sum(dfs(root, 0))


def dfs(tn, s):
    if tn:
        s = s * 2 + tn.val
        if not tn.left and not tn.right:
            yield s
        else:
            yield from dfs(tn.left, s)
            yield from dfs(tn.right, s)
