class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i =0
        j =0
        curr_sum = 0
        ans = float('inf')
        n = len(nums)
        while j < n:

            #expand window
            curr_sum += nums[j]
            j += 1


            while curr_sum >= target:
                window = j - i
                ans = min(ans, window)

                curr_sum -= nums[i]
                i += 1
            
        return ans if ans != float('inf') else 0


