class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0

        for i in range(len(nums)):
            # if current is beyond maxReach
            if i > maxReach:
                return False
            
            #update maxReach to farthest position
            maxReach = max(maxReach, i + nums[i])

            #if already reached end, early exit
            if maxReach > len(nums) - 1:
                return True
            
        return True




