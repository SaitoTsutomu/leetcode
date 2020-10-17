# %% [997. Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/submissions/)
# 問題：判事を返せ
# 解法：すべての人に信用されている人が誰も信用してなければ判事
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust:
            return 1 if N == 1 else -1
        c1, c2 = map(collections.Counter, zip(*trust))
        p, n = c2.most_common(1)[0]
        return p if n == N - 1 and not c1.get(p) else -1
