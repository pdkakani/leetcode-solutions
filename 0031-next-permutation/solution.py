class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # step 1: find the pivot from right to left

        i = len(nums) - 2

        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        # find the swap position
        if i >= 0:
            j = len(nums) - 1
            while j > 0 and nums[j] <= nums[i]:
                j -= 1
        
            # perform the swap
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse the sequqnce after pivot position
        nums[i+1:] = reversed(nums[i+1:])


