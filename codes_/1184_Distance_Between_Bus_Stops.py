# %% [1184. Distance Between Bus Stops](https://leetcode.com/problems/distance-between-bus-stops/)
# 問題：サイクル上の距離（distance）を使いstart、destination間の距離を返せ
# 解法：時計回りと反時計回りの短い方
class Solution:
    def distanceBetweenBusStops(
        self, distance: List[int], start: int, destination: int
    ) -> int:
        a = min(start, destination)
        b = max(start, destination)
        return min(sum(distance[a:b]), sum(distance) - sum(distance[a:b]))
