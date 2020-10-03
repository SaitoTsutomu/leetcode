# %% [941. Valid Mountain Array](https://leetcode.com/problems/valid-mountain-array/)
# 問題：前半単調増加して後半単調減少しているかを返せ
# 解法：itertools.takewhileを用いる
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        df = [j - i for i, j in zip(A, A[1:])]
        n = len(list(itertools.takewhile(lambda x: x > 0, df)))
        return n > 0 and n < len(df) and all(y < 0 for y in df[n:])
