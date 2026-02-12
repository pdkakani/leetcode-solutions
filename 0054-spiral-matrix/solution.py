class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        row_len = len(matrix)
        col_len = len(matrix[0])

        top = 0
        bottom = row_len -1
        left = 0
        right = col_len - 1
        result = []

        while top <= bottom and left <= right:

            # move left along top
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1


            # move down alogn right
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1


            # move left along bottom
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
            

            # move top along left
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
            
        return result

            

        
