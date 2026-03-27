class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []
        def bt(start):
            res.append(list(path)) #collect at every node
            for i in range(start, len(nums)):
                path.append(nums[i])
                bt(i + 1) # never go backwards
                path.pop()
        bt(0)
        return res
        
