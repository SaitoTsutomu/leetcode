# %% [228. Summary Ranges](https://leetcode.com/problems/summary-ranges/)
# 問題：numsの連続する部分リストは'a->b'のようにせよ
# 解法：resに、1より増えたら[]を追加し、resの最後の[1:]を更新する
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        for num in nums:
            if not res or num > res[-1][-1] + 1:
                res.append([])
            res[-1][1:] = (num,)
        return ["->".join(map(str, i)) for i in res]
