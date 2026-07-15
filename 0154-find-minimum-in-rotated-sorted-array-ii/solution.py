class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        # res = float('inf')

        # while left <= right:
        #     if nums[left] < nums[right]:
        #         res = min(res, nums[left])
            
        #     mid = (left + right) // 2
        #     res = min(res, nums[mid])
        #     if nums[mid] > nums[left]:
        #         left = mid + 1
        #     elif nums[mid] < nums[left]:
        #         right = mid - 1
        #     else:
        #         left += 1

        # return res

        while left < right:
            mid = (left + right) //2 
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1

        return nums[left]


        
        
