# %% [976. Largest Perimeter Triangle](https://leetcode.com/problems/largest-perimeter-triangle/)
# 問題：三角形になりうる最大の3辺の和を返せ
# 解法：sortする
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        a = sorted(A)
        while len(a) >= 3:
            if a[-1] < a[-2] + a[-3]:
                return sum(a[-3:])
            a.pop()
        return 0


def dfs(tn, v):
    return not tn or tn.val == v and dfs(tn.left, v) and dfs(tn.right, v)
