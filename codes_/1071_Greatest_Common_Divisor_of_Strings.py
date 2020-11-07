# %% [1071. Greatest Common Divisor of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/)
# 問題：str1とstr2を分割する文字列を返せ（存在しないときは空文字列）。s = t * nのときtはsを分割する
# 解法：math.gcdを用いる
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n = math.gcd(n1 := len(str1), n2 := len(str2))
        s = str1[:n]
        return s * (s * (n1 // n) == str1 and s * (n2 // n) == str2)
