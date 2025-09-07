class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            # shrink the window from the left if the char is found
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            # Add new char and update result
            seen.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length
        
