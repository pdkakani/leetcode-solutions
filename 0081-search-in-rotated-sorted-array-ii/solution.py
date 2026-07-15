class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            
            # is left half sorted ?
            if nums[mid] > nums[right]:
                # is target in left sorted half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            elif nums[mid] < nums[right]:
                # is target in right sorted half
                if nums[right] >= target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                right -= 1

        return False
