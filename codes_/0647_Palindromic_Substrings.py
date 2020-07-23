# %% [647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        return sum(count_palindromic_from_center(s[i:j], j - i)
            for i, j in itertools.chain(
                [(0, k + 1) for k in range(n)], [(k, n) for k in range(1, n)]))

def count_palindromic_from_center(s, n):
    f = lambda i: s[i] == s[n - i - 1]
    return n % 2 + len(list(itertools.takewhile(f, range((n - 2) // 2, -1, -1))))
