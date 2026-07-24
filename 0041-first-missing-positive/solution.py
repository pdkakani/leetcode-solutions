class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # neutralize all negatives since we are using sign marking method here
        n = len(nums)
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0

        # apply the sign marking method to later find if the element from our solution set is in input or not
        for i in range(n):
            # always use abs value to calc index since we would be changing signs
            index = abs(nums[i]) - 1 

            # check for bounds
            if index >= 0 and index < n:
                if nums[index] == 0:
                    # change it to something along with sign change which doesnt interfere with the input values
                    nums[index] = -1 * (n + 1)
                elif nums[index] > 0:
                    # change the sign to mark that the index number exists
                    nums[index] = -1 * nums[index]
        
        # next we loop over our solution range to find the answer
        for i in range(1, n + 1):
            if nums[i - 1] >= 0:
                # if yes, that means we havent seen this number in our input array so return 
                return i
        
        # if we dont return from the loop above, the we return the next smallest positive which is 
        return n + 1
