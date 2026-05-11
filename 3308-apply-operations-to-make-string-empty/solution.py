class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        freq = Counter(s)
        max_freq = max(freq.values())

        res = ""

        for c in s:
            if freq[c] == max_freq:
                res = res.replace(c,"")
                res += c
            
        return res
        
