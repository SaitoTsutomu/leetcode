# %% [1013. Partition Array Into Three Parts With Equal Sum](https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/)
# 問題：3つのグループの和が等しくなるように2箇所で区切れるかを返せ
# 解法：和の1/3に等しい回数を数える
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = sum(A)
        c, cs, s3 = 0, 0, s // 3
        for a in A:
            if (cs := cs + a) == s3:
                c, cs = c + 1, 0
        return c >= 3
