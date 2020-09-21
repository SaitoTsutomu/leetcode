# %% [914. X of a Kind in a Deck of Cards](https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/)
# 問題：すべてサイズがX（>2）で同一の数からなるグループに分割できるかを返せ
# 解法：math.gcdを用いる
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        return functools.reduce(math.gcd, collections.Counter(deck).values()) >= 2
