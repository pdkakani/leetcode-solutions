class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        extended_code = code * 2
        if k > 0:
            result = []
            for i in range(n):
                window = extended_code[i+1:i+1+k]
                total = sum(window)
                result.append(total)
            return result
        else:
            k = abs(k)
            result = []
            for i in range(n):
                window = extended_code[i+n-k:i+n]
                total = sum(window)
                result.append(total)
            return result    

        
