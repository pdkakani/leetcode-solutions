class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        res = []

        for i in range(len(nums)):
            # remove expired index from front
            if d and d[0] <= i - k:
                d.popleft()

            #remove smaller elements from the back
            while d and nums[d[-1]] < nums[i]:
                d.pop()
            
            d.append(i)

            # start recording once first window is complete
            if i >= k - 1:
                res.append(nums[d[0]])
            
        return res


