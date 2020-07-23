# %% [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s := s.lower()) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i] != s[j]:
                return False
            i, j = i + 1, j - 1
        return True
