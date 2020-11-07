# %% [1103. Distribute Candies to People](https://leetcode.com/problems/distribute-candies-to-people/)
# 問題：num_people人にcandies個のキャンディーを分けて分配数を返せ。n番目はn個配る
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        a, b, d = 0, 0, [0] * num_people
        while candies := candies - a:
            a = min(candies, b := b + 1)
            d[(b - 1) % num_people] += a
        return d
