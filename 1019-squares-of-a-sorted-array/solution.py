class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        res = [0] * len(nums)
        curr = len(nums) - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res[curr] = nums[left] ** 2
                left +=1
            else:
                res[curr] = nums[right] ** 2
                right -= 1
            curr -= 1

        return res   

