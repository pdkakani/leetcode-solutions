class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        nums.sort()

        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            low = i+1
            high = n -1
            while low < high:
                curr_sum = nums[i] + nums[low] + nums[high]
                if curr_sum == 0:
                    result.append([nums[i], nums[low], nums[high]])
                    low += 1
                    high -=1
                    while low < high and nums[low] == nums[low -1]:
                        low+=1
                    while low< high and nums[high] == nums[high + 1]:
                        high-=1
                elif curr_sum < 0:
                    low += 1
                else:
                    high -= 1
        return result 
        
