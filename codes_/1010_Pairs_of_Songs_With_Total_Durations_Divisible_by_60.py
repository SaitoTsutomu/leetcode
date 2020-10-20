# %% [1010. Pairs of Songs With Total Durations Divisible by 60](https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/)
# 問題：60の倍数となるtimeの2つの要素のペア数を返せ
# 解法：collections.Counterを用いる
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        c = collections.Counter([t % 60 for t in time])
        return (
            sum(n * (c.get(60 - t, 0) if t % 30 else n - 1) for t, n in c.items()) // 2
        )
