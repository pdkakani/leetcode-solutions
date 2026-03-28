class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, path = [],[]
        candidates.sort()
        def bt(start, rem):
            if rem == 0:
                res.append(list(path))
                return
            
            for i in range(start, len(candidates)):
                if candidates[i] > rem:
                    break
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                path.append(candidates[i])
                bt(i, rem - candidates[i])
                path.pop()

        bt(0, target)
        return res
        
