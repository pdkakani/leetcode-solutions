class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # def get_closest(num):
        #     return abs(x - num)
        
        # heap = []
        # for num in arr:
        #     heapq.heappush(heap, (-get_closest(num), -num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # print(heap)
            
        # return sorted([-num[1] for num in heap])

        left = 0
        right = len(arr) - k

        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]

        
