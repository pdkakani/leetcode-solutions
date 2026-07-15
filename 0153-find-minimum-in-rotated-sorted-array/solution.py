class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        res = float('inf')
        # while left <= right:
        #     if nums[left] < nums[right]:
        #         # that means its already sorted
        #         res = min(res, nums[left]) # because smallest will alwasy be to the left in sorted list

        #     mid = (left + right) // 2
        #     res = min(res,  nums[mid])
        #     if nums[mid] >= nums[left]:
        #         # that means minimum is to the right
        #         left = mid + 1
        #     else:
        #         right = mid - 1

        # return res

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
        return nums[left]


        
