class Solution:
    def mirrorFrequency(self, s: str) -> int:
        alnum_map = {"a":"z", "b":"y", "c":"x", "d":"w",
                       "e":"v", "f":"u", "g":"t", "h":"s", 
                      "i":"r", "j":"q", "k":"p", "l":"o",
                      "m":"n", "0":"9", "1":"8", "2":"7", "3":"6",
                      "4":"5"}

        res = 0
        freq = Counter(s)
        for k, v in alnum_map.items():
            res += abs(freq[k] - freq[v])
                

        return res
        
