class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if s == '': return True
        ns = len(s)
        nt = len(t)
        if ns > nt: return False
        i = 0
        j = 0

        count = 0

        while j < nt and i < ns:
            if s[i] == t[j]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1
        
        return count == ns


        
