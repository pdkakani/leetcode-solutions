class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        res = float("inf")
        currSum = 0
        for right in range(len(nums)):
            currSum += nums[right]

            while currSum >= target:
                res = min(res, right - left + 1)
                currSum -= nums[left]
                left += 1
            
            
        return res if res != float("inf") else 0


        
