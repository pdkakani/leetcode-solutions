class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        i = 0
        d = len(s)
        result = []
        
        for k in s:
            if k == "I":
                result.append(i)
                i+=1
            elif k == "D":
                result.append(d)
                d-=1
        result.append(i)    
        return result
        
