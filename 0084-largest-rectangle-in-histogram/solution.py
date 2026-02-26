class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:    
                right = i
                top = stack.pop()
                left = stack[-1] if stack else -1 
                width = (right-left) - 1
                height = heights[top]
                max_area = max(max_area, width * height)
            stack.append(i)

        while stack:
            right = len(heights)
            top = stack.pop()
            left = stack[-1] if stack else -1
            width = right -left - 1
            height = heights[top]
            max_area = max(max_area, width * height) 

        return max_area 
        
