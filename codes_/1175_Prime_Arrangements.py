# %% [1175. Prime Arrangements](https://leetcode.com/problems/prime-arrangements/)
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        p1 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
        p2 = [43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        np = bisect.bisect(p1 + p2, n)
        return math.factorial(np) * math.factorial(n - np) % (10 ** 9 + 7)
