class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        result = float('inf')
        if len(nums) < 2:
            return 0

        sorted_nums = sorted(nums, reverse=True)
        for i in range(len(nums)-k+1):
            minimum = sorted_nums[i] - sorted_nums[i+k-1]
            result = min(minimum, result)
        return result
