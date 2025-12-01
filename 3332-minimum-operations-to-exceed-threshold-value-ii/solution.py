class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        count = 0

        while nums[0] < k:
            a = heapq.heappop(nums)
            b = heapq.heappop(nums)
            temp = min(a,b) * 2 + max(a,b)
            heapq.heappush(nums, temp)
            count += 1
        return count

            






        
        
