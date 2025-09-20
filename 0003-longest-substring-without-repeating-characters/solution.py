class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        n = len(s)
        longest = 0

        for right in range(n):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            w = (right - left) + 1
            longest = max(w, longest)
            seen.add(s[right])

        return longest
        
