class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = []
        for start, end in intervals:
            events.append((start, 1))
            events.append((end, -1))
        
        
        events.sort()
        rooms = 0
        max_rooms = 0

        for time, change in events:
            rooms += change
            max_rooms = max(max_rooms, rooms)
        return max_rooms
        
