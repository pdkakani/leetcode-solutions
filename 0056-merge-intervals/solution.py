class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        start, end = intervals[0]

        res = []
        for i in range(1, len(intervals)):
            next_start, next_end = intervals[i]

            if end >= next_start:
                start = min(start, next_start)
                end = max(end, next_end)
            elif end < next_start:
                res.append([start, end])
                start = next_start
                end = next_end

        res.append([start,end])
        return res
        
