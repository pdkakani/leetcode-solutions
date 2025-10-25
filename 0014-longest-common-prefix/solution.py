class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = min(strs)
        n = len(smallest)
        i = 0

        while i < n:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i+=1

        return strs[0][:i]
                

        

        
