class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            # convert number into zero based index
            index = abs(num) - 1

            # mark index as visited
            nums[index] = -abs(nums[index])

        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)

        return ans

        
