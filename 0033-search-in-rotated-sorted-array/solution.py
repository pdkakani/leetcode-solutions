class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -=1
            # if true then left is sorted
            elif nums[left] <= nums[mid]:
                # check if the target is within the left part
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # right part is sorted
                # check if the target is within the right part
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1
                 


