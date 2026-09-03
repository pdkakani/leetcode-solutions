class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        ns, ne = newInterval
        n = len(intervals)

        i = 0
      

        # if the new interval in after the current interval
        while i < n and ns > intervals[i][1]:
            res.append(intervals[i])
            i += 1

        # if the new interval overlaps the current interval
        while i < n and ne >= intervals[i][0] and ns <= intervals[i][1]:
            ns = min(intervals[i][0], ns)
            ne = max(intervals[i][1], ne)
            i += 1
        res.append([ns, ne])

        # if the new intervals in before the current interval
        while i < n and ne < intervals[i][0]:
            res.append(intervals[i])
            i += 1
        return res

        
