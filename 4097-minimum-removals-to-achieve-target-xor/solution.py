class Solution:
    def minRemovals(self, nums: List[int], target: int) -> int:
        inp = nums
        n = len(nums)
        # dp[xor_val] = max elements we can KEEP with that xor value
        dp = {0: 0}
        
        for num in nums:
            new_dp = dict(dp)  # start with not taking current num
            for xor_val, count in dp.items():
                new_xor = xor_val ^ num
                if new_xor not in new_dp or new_dp[new_xor] < count + 1:
                    new_dp[new_xor] = count + 1
            dp = new_dp
        
        if target not in dp:
            return -1
        
        return n - dp[target]
