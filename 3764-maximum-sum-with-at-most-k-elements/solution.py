class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        res = []

        rows = len(grid)
        cols = len(grid[0])

        for i in range(len(limits)):
            temp = grid[i]
            temp.sort(reverse = True)
            for j in range(limits[i]):
                res.append(temp[j])

        total = 0
        res.sort(reverse=True)

        print(res)
        for i in range(k):
            total += res[i]

        return total
            
        
