class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            h[nums[i]] = i

        for i in nums:
            temp = target - i
            if temp in h and nums.index(i) != h[temp]:
                return [nums.index(i), h[temp]]

        
