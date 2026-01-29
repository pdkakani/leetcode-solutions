class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        posToUpdate = 0
        currentElem = None
        occurrences = 1
        threshold = 2
        for num in nums:
            if (num != currentElem):
                currentElem = num
                occurrences = 1
            else:
                occurrences += 1
            if (occurrences <= threshold):
                nums[posToUpdate] = num
                posToUpdate += 1
        return posToUpdate
        
