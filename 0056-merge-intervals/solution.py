class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(intervals)
        
        intervals.sort(key = lambda interval: interval[0])
        
        prev = intervals[0]
        for i in range(1, n):
            if intervals[i][0] <= prev[1]:
                prev[1] = max(prev[1], intervals[i][1]) 
            else:
                ans.append(prev)
                prev = intervals[i]
        ans.append(prev)
        return ans
