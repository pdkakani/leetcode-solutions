class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]

        def get_common_prefix(s1, s2):
            i = 0
            while i < min(len(s1), len(s2)) and s1[i] == s2[i]:
                i += 1
            return s1[:i]
        
        for s in strs[1:]:
            prefix = get_common_prefix(prefix, s)
        return prefix
        
