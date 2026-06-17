class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # sorted by deadline
        sorted_courses = sorted(courses, key= lambda x:x[1])

        dur = 0
        heap = []


        for c_dur, deadline in sorted_courses:
            dur += c_dur
            heapq.heappush(heap, -c_dur)
            if dur > deadline:
                largest_dur = heapq.heappop(heap)
                dur += largest_dur
        
        return len(heap)


        
