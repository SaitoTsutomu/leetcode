# %% [953. Verifying an Alien Dictionary](https://leetcode.com/problems/verifying-an-alien-dictionary/)
# 問題：wordが辞書順かどうかを返せ。ただし文字はorder順とする
# 解法：単語を順番のリストに変換
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dc = {c: i for i, c in enumerate(order)}
        lst = [[dc[c] for c in word] for word in words]
        return all(i <= j for i, j in zip(lst, lst[1:]))
