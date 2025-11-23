class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        n = len(s)
        res = 0

        for right in range(n):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            w = right - left + 1
            res = max(res, w)
            seen.add(s[right])
        return res


        
