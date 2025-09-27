class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        seen = {}
        result = []
        for i in p:
            seen[i] = seen.get(i, 0) + 1
        count = len(seen)

        i = 0
        j = 0
        while j < len(s):
            # calculations
            if s[j] in seen:
                seen[s[j]] -= 1
                if seen[s[j]] == 0:
                    count -= 1
            window = (j - i) + 1
            if window < len(p):
                j += 1
            if window == len(p):
                if count == 0:
                    result.append(i)
                # remove calculation before sliding the window
                if s[i] in seen:
                    seen[s[i]] = seen.get(s[i]) + 1
                    if seen.get(s[i]) == 1:
                        count += 1
                i += 1
                j += 1
        return result 

        
