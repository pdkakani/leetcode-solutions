class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for curr in intervals:
            # if curr ends before new starts
            if curr[1] < newInterval[0]:
                res.append(curr)
            # if curr starts after new ends
            elif curr[0] > newInterval[1]:
                res.append(newInterval)
                newInterval = curr
            else:
                newInterval[0] = min(curr[0], newInterval[0])
                newInterval[1] = max(curr[1], newInterval[1])
            
        res.append(newInterval)
        return res

        return res
        
