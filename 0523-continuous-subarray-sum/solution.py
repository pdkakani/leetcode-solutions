class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainders = {0:-1}
        running = 0
        for i in range(len(nums)):
            running += nums[i]
            rem = (running % k)
            if rem in remainders:
                if i - remainders[rem] >= 2:
                    return True
            else:
                remainders[rem] = i
        return False
        
