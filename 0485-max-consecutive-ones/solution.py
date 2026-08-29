class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # best = 0
        # count = 0

        # for num in nums:
        #     if num == 0:
        #         count = 0
        #         continue
        #     count += 1
        #     best = max(best, count)


        # return best

        left = 0
        res = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                left = right + 1
                continue
            
            res = max(res, right - left + 1)

        return res
        
