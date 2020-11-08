# %% [1170. *Compare Strings by Frequency of the Smallest Character](https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/)
# 問題：f(s)をsの最小の文字のsでの出現数とする。queriesの各要素queryごとの計算値をリストで返せ。計算値はwordsの各要素wordがf(query) < f(word)となる個数
# 解法：ソートしたものにbisect.bisectを用いる（線形探索より高速）
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        cc = [query.count(min(query)) for query in queries]
        ww = sorted(word.count(min(word)) for word in words)
        return [len(ww) - bisect.bisect(ww, c) for c in cc]
