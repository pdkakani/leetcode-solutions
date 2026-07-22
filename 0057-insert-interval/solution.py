class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ns, ne = newInterval
        n = len(intervals)
        i = 0
        res = []

        while i < n and intervals[i][1] < ns:
            res.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= ne and intervals[i][1] >= ns:
            ns = min(intervals[i][0], ns)
            ne = max(intervals[i][1], ne)
            i+=1
        res.append([ns,ne])
        
        while i < n and intervals[i][0] > ne:
            res.append(intervals[i])
            i += 1
        
        return res

        
