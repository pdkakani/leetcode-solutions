class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []

        for right in range(len(nums)):
            heapq.heappush(heap, (-nums[right], right))

            while heap[0][1] <= right - k:
                heapq.heappop(heap)
            
            if right >= k - 1:
                res.append(-heap[0][0])
            
        return res
        
