# %% [989. Add to Array-Form of Integer](https://leetcode.com/problems/add-to-array-form-of-integer/)
# 問題：AとKの和をリストで返せ
# 解法：下位の桁から加算
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        k, res, B = 0, [], [int(c) for c in str(K)]
        for i, j in itertools.zip_longest(A[::-1], B[::-1], fillvalue=0):
            n = i + j + k
            res.append(n % 10)
            k = n // 10
        if k:
            res.append(k)
        return list(reversed(res))
