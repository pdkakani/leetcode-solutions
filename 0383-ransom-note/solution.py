class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom = Counter(ransomNote)
        mag = Counter(magazine)

        for i, j in ransom.items():
            if i in mag and mag[i] >= j:
                continue
            else:
                return False
        return True



        
