class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #search over indices

        def first_occ(nums, target):
            left = 0
            right = len(nums)


            while left < right:
                mid = left + (right -left) // 2

                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return left

        def last_occ(nums, target):
            left = 0
            right = len(nums)

            while left < right:
                mid = left + (right - left) // 2

                if nums[mid] > target:
                    right = mid
                else:
                    left= mid + 1
            return left - 1


        first = first_occ(nums, target)
        if first == len(nums) or nums[first] != target:
            return [-1,-1]
        last = last_occ(nums, target)
        return [first, last]


        
