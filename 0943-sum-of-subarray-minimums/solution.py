class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # Brute force
        MOD = 10 ** 9 + 7
        # n = len(arr)
        
        # total = 0
        # for start in range(n):
        #     curr_min = arr[start]
        #     for end in range(start, n):
        #         if arr[end] < curr_min:
        #             curr_min = arr[end]
        #         total += curr_min
        # return total % MOD
        

        n = len(arr)

        left_block = [-1] * n
        right_block = [n] * n
        total = 0
        stack = []

        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            if stack:
                left_block[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            
            if stack:
                right_block[i] = stack[-1]
            
            stack.append(i)
        

        for i in range(n):
            a = i - left_block[i]
            b = right_block[i] - i

            count = a*b

            total += arr[i] * count
        
        return total % MOD
        
