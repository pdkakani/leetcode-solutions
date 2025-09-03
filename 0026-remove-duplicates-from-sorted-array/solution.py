class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        j=1
        while j < len(nums):
            if nums[i] == nums[j]:
                j=j+1
            elif nums[i] != nums[j]:
                i=i+1
                nums[i] = nums[j]
        return len(set(nums))
                


        
