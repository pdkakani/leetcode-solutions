class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        best = 0

        for x in nums_set:
            if x - 1 not in nums_set:
                temp = x
                res = 1

                while temp + 1 in nums_set:
                    res+= 1
                    temp += 1
                
                best = max(best, res)
        
        return best
        
