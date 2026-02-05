class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        inp = s.split()
        return len(inp[-1].strip())
