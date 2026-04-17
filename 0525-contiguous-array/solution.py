class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        seen = {0:0}
        prefix = 0
        res = 0

        for i in range(len(nums)):
            prefix += (-1) if nums[i] == 0 else 1

            if prefix not in seen:
                seen[prefix] = i+1
            else:
                res = max(res, (i+1) - seen[prefix])
        
        return res
