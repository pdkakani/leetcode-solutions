class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # heap = []
        # count = Counter(nums)

        # for v, f in count.items():
        #     heapq.heappush(heap, (f,v))
        #     if len(heap) > k:
        #         heapq.heappop(heap)

        # return [val for f, val in heap]
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key = lambda x: (count[x]))
