# %% [1089. Duplicate Zeros](https://leetcode.com/problems/duplicate-zeros/)
# 問題：arrの要素が0の場合に直後に0を追加せよ。arrそのものを変更せよ。長さが同じになるように切り詰めよ
# 解法：ジェネレーターを用いる
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        arr[:] = list(conv(arr))[: len(arr)]


def conv(arr):
    for i in arr:
        yield i
        if not i:
            yield i
