# %% [169. *Majority Element](https://leetcode.com/problems/majority-element/)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return collections.Counter(nums).most_common(1)[0][0]
