class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 1
        block_start = nums[0]

        for j in range(1, len(nums)):
            if nums[j] - block_start > k:
                res += 1
                block_start = nums[j]
        return res
