class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}

        # build the next greater mapping for all elements in nums2:
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        
        ans = []
        for x in nums1:
            ans.append(next_greater.get(x, -1))
        return ans
                
            

        
