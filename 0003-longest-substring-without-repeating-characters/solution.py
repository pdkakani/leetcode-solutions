class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        n = len(s)
        i = 0
        j = 0
        ans = 0

        while j < n:

            while s[j] in seen:
                seen.remove(s[i])
                i += 1

            
            
            seen.add(s[j])
            j += 1
            
           
            ans = max(ans, j - i)

            
        return ans

