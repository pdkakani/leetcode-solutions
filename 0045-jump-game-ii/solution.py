class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        farthest = 0
        n = len(nums)
        cur_end = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])

            if i == cur_end:
                res += 1
                cur_end = farthest

                if cur_end > n:
                    break
            
        return res
        
