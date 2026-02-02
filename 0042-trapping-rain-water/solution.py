class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n
        right = [0] * n
        res = 0

        prefix = 0
        for i in range(0,n):
            prefix = max(height[i], prefix)
            left[i] = prefix

        suffix = 0
        for i in range(n-1,-1,-1):
            suffix = max(height[i], suffix)
            right[i] = suffix

        for i in range(n):
            res += min(left[i], right[i]) - height[i]

        return res 


        

