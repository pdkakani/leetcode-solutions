class Solution:
    def isPalindrome(self, s: str) -> bool:
        # first step is to clean the string
        cleaned = ""
        for i in s.lower():
            if i.isalnum():
                cleaned += i

        left = 0
        right = len(cleaned) - 1

        while left <= right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1
        return True
        
