class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if not any(i % 2 != 0 for i in nums1) or min(nums1) % 2 != 0:
            return True
        return False
