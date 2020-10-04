# %% https://leetcode.com/problemset/algorithms/?difficulty=Easy&status=Todo
from leetcode import *  # noqa


# %% [961. N-Repeated Element in Size 2N Array](https://leetcode.com/problems/n-repeated-element-in-size-2n-array/)
# 問題：N回繰り返している数を返せ
# 解法：余計なものは「len(A) // 2 - 1」個
class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        return (sum(A) - sum(set(A))) // (len(A) // 2 - 1)


# %%
Solution().isLongPressedName("alex", "aaleex")


# %%
