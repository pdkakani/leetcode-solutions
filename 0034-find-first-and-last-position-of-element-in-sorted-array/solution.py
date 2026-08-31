class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def bs(nums, target, findFirst):
            left = 0
            right = len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2
                if target > nums[mid]:
                    left = mid + 1
                elif target < nums[mid]:
                    right = mid - 1
                else:
                    ans = mid
                    if findFirst:
                        right = mid - 1
                    else:
                        left = mid + 1
            return ans
        return [bs(nums, target, True), bs(nums, target, False)]

        
