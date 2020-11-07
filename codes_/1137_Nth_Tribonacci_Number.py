# %% [1137. *N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/)
# 問題：T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2となるTを返せ
# 解法：collections.dequeを用いる
class Solution:
    def tribonacci(self, n: int) -> int:
        d = collections.deque([1, 0, 0], maxlen=3)
        for _ in range(n):
            d.append(sum(d))
        return d[-1]
