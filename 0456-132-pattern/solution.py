class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # the focus is to find nums[k]
        # we will maintain a stack [num, currMin]

        # maintain a decreasing montonic stack because I want the max to be on top
        stack = []
        currMin = nums[0]

        for n in nums[1:]:
            while stack and n >= stack[-1][0]:
                stack.pop()

            # if stack and n is greater than curr_min, i.e. we have found our nums[k]
            if stack and n > stack[-1][1]:
                return True
            
            stack.append([n, currMin])
            currMin = min(currMin, n)
        return False
        
