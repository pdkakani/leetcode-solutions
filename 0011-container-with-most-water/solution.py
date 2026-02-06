class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1 
        ans = 0

        # vertically find the two tallest heights which has max distance between them
        while i < j:
            left = height[i]
            right = height[j]

            distance = j - i

            temp_ans = distance * min(left, right)
            ans = max(ans, temp_ans)

            if left < right:
                i += 1
            else:
                j -= 1
            
        return ans        
