# %% [1018. Binary Prefix Divisible By 5](https://leetcode.com/problems/binary-prefix-divisible-by-5/)
# 問題：各要素までを2進数とみなし5で割り切れるかを返せ
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        i = 0
        for a in A:
            i = i * 2 + a
            yield not i % 5
