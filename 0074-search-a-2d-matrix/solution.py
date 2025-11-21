class Solution:
    def binarySearch(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return 99999
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return nums[right]

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        left = 0
        right = n-1

        while left <= right:
            mid = (left + right) // 2
            res = self.binarySearch(matrix[mid], target)
            if res == 99999:
                return True
            elif res > target:
                right = mid - 1
            elif res < target:
                left = mid + 1
        return False

    

