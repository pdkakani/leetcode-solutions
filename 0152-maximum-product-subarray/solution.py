class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_min = nums[0]
        curr_max = nums[0]
        best = nums[0]

        for i in range(1, len(nums)):
            candidates = (nums[i], curr_max * nums[i], curr_min * nums[i])
            curr_max = max(candidates)
            curr_min = min(candidates)
            best = max(best, curr_max)
    
        return best


