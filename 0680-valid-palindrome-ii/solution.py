class Solution:
    def isPal(self, st:str) -> bool:

            left = 0
            right = len(st) - 1

            while left < right:
                if st[left] != st[right]:
                    return False
                left += 1
                right -= 1
            return True

    def validPalindrome(self, s: str) -> bool:
        if self.isPal(s):
            return True

        i = 0
        j = len(s)

        while i < j:
            if s[i] != s[j-1]:
                return self.isPal(s[i+1: j]) or self.isPal(s[i:j-1])
            i += 1
            j -= 1


        
        return True


        


        
