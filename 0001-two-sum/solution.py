class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        for i in range(len(nums)):
            h[nums[i]] = i

        for i in range(len(nums)):
            temp = target - nums[i]

            if temp in h and h[temp] != i:
                return [i, h[temp]]
