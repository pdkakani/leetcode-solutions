class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        cur_sum = sum(nums[0:k])
        max_sum = cur_sum


        for r in range(k, n):
            cur_sum += nums[r]
            cur_sum -= nums[r - k]
            if cur_sum > max_sum:
                max_sum = cur_sum
            
            
            
            
        return max_sum/k

