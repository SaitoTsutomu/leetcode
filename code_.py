# %% [350. Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = collections.Counter(nums1) & collections.Counter(nums2)
        return list(c.elements())


# %%
Solution().intersect([1, 2, 2, 1], [4, 2, 2])
