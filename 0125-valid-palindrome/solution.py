class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ""

        for c in s:
            if c.isalnum():
                clean_s += c

        lower_cs = clean_s.lower()
        return lower_cs[::-1] == lower_cs

