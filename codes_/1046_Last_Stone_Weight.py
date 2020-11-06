# %% [1046. Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)
# 問題：stonesから2つの大きい要素を取り、差が0でなければ差を戻す。最後の1つ（空なら0）を返せ
# 解法：heapqを用いる
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        a = [-i for i in stones]
        heapq.heapify(a)
        while a:
            b = heapq.heappop(a)
            if not a:
                return -b
            c = heapq.heappop(a)
            if b < c:
                heapq.heappush(a, b - c)
        return 0
