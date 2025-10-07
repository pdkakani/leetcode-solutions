class Solution:

    def isIncreasing(self, n:List[int]) -> bool:
        for j in range(1, len(n)):
            if n[j] < n[j -1]:
                return False
        return True

    def minimumPairRemoval(self, nums: List[int]) -> int:
        
        count = 0
        
        while not self.isIncreasing(nums):
            n = len(nums)
            min_sum = float('inf')
            j = 0
            for i in range(0, n-1):
                if nums[i] + nums[i+1] < min_sum:
                    min_sum = nums[i] + nums[i+1]
                    j = i
                
            nums[j] = nums[j] + nums[j+1]
            del nums[j+1]
            count+=1
        return count
        
