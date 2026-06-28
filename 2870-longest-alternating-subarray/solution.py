class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        
        
        best = -1
        i = 0
        while i < n -1:
            if nums[i + 1] - nums[i] != 1:
                i += 1
                continue
            
            j = i + 1
            while j < n -1 and nums[j + 1] - nums[j] == -(nums[j] - nums[j-1]):
                j += 1
            

            best = max(best, j - i + 1)
            i = j
        return best

        


        
