class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x: x[0])
        n = len(intervals)
        if n < 1:
            return True
        start, end = intervals[0]
        for i in range(1, n):
            next_start, next_end = intervals[i]

            if end > next_start:
                return False
            else:
                start = next_start
                end = next_end
        
        return True
            
        
