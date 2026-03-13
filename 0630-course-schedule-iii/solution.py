class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        
        #sorted courses by deadline
        sorted_c = sorted(courses, key = lambda x: x[1])

        dur = 0
        heap = []

        for c in sorted_c:
            d, last = c
            heappush(heap, -d)

            dur += d

            if dur > last:
                largest_dur = heappop(heap)
                dur += largest_dur # (+ because its heap value negated)
            
        return len(heap)

            

