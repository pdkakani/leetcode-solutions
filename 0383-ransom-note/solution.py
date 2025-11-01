class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = Counter(ransomNote)
        m = Counter(magazine)

        for k,v in r.items():
            if m[k] is None or m[k] < v:
                return False

        return True 


        
