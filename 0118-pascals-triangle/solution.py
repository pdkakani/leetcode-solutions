class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        
        triangle = self.generate(numRows - 1)
        lastRow = triangle[-1]
        newRow = [1]

        for i in range(len(lastRow) - 1):
            newRow.append(lastRow[i] + lastRow[i+1])

        newRow.append(1)

        triangle.append(newRow)
        return triangle

