class Solution:
    def reverseWords(self, s: str) -> str:
        # first convert the string into words of array separated by space
        words = s.split()
        result = ""

        left = 0
        right = len(words) - 1
        while left <= right:
            temp = words[left]
            words[left] = words[right]
            words[right] = temp
            left += 1
            right -= 1
        
        return " ".join(words)
        
