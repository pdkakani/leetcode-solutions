class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < nums[mid + 1]:
                left = mid + 1 # peak is at the right
            else:
                right = mid # peak is at the left or mid
        return left


        
