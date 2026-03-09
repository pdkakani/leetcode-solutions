class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # flatten_list = [i for sublist in matrix for i in sublist]
        # flatten_list.sort()
        # return flatten_list[k - 1]
        n = len(matrix)
        low = matrix[0][0]
        high = matrix[n -1][n-1]
        

        def count_less_equal(mid):
            count = 0
            row = n - 1 #start at bottom
            col = 0 #start at left

            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    count += row + 1
                    col += 1 # move right
                else:
                    row -= 1 # move up
            return count

        while low < high:
            mid = (low + high) // 2
            if count_less_equal(mid) >= k:
                high = mid
            else:
                low = mid + 1
        return low 



        
