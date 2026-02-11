class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if not s or not t:
            return ""

        tCounter = Counter(t)
        i = 0
        j = 0
        
        res = ""
        min_len = float('inf')
        current_count = Counter()

        while j < len(s):
            # expand
            current_count[s[j]] += 1


            # check window condition
            while not (tCounter - current_count):
                # if window valid, record the answer
                window = j - i + 1
                if window < min_len:
                    min_len = window
                    res = s[i:j+1]
                
                current_count[s[i]] -= 1
                i += 1
            j += 1
        return res
