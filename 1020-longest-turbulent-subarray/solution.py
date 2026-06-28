class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        best = 1            # a single element is always turbulent (length 1)
        run = 1             # current turbulent run length
        prev = 0            # previous direction: +1 up, -1 down, 0 equal/none

        for i in range(1, n):
            # figure out current direction
            if arr[i] > arr[i-1]:
                cur = 1
            elif arr[i] < arr[i-1]:
                cur = -1
            else:
                cur = 0

            if cur == 0:
                run = 1
            elif cur == prev:
                run = 2
            else:
                run = run + 1

            best = max(best, run)
            prev = cur
        return best
        

            
        
