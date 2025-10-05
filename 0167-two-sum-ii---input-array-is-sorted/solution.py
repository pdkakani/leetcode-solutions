class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1 
        result = []

        while i < j:
            curr_sum = numbers[i] + numbers[j]
            if curr_sum == target:
                result.append(i+1)
                result.append(j+1)
                break
            if curr_sum < target:
                i += 1
            if curr_sum > target:
                j -= 1
            
        return result

        
