class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def get_dist(point):
            return point[0] ** 2 + point[1] ** 2

        heap = []
        for p in points:
            heapq.heappush(heap, (-get_dist(p),p))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [point[1] for point in heap]
            

        
