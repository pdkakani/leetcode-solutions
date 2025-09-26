class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        
        minimum = float('inf')
        

        for k in range(l, r+1):
            i = 0
            j = 0
            curr_sum = 0
            while j < len(nums):
                curr_sum += nums[j]
                window = (j - i) + 1
                if window < k:
                    j += 1
                elif window == k:
                    if curr_sum > 0:
                        minimum = min(minimum, curr_sum)
                    curr_sum -= nums[i]
                    i += 1
                    j += 1
        if minimum == float('inf') or minimum < 0:
            return -1
        return minimum
            
        
