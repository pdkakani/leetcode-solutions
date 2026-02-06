class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res = haystack.find(needle, 0, len(haystack))
 
        return res if res >= 0 else -1
        
