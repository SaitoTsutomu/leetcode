# %% [985. Sum of Even Numbers After Queries](https://leetcode.com/problems/sum-of-even-numbers-after-queries/)
# 問題：queriesを適用するごとに偶数の要素の和のリストを返せ
# 解法：クエリの更新位置だけ偶数の要素の和を更新
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        es = sum(i for i in A if not i % 2)
        return [es := calc(A, v, i, es) for v, i in queries]


def calc(A, v, i, es):
    if not A[i] % 2:
        es -= A[i]
    A[i] += v
    if not A[i] % 2:
        es += A[i]
    return es
