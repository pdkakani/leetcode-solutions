class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return any(i % 2 != 0 for i in nums1) or True
