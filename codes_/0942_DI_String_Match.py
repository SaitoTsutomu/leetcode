# %% [942. *DI String Match](https://leetcode.com/problems/di-string-match/)
# 問題：IかDで構成されるSから[0, 1, 2, ..., n-1]を入れ替えたリストを返せ。リストの増減がI、Dに対応する
# 解法：2つのiter(range(...))をnextする
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        ri, rd = iter(range((n := len(S)) + 1)), iter(range(n, -1, -1))
        return [next(rd) if c == "D" else next(ri) for c in S] + [next(rd)]
