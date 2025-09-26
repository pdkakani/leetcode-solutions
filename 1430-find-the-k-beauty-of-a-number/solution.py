class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        i = 0
        j = 0
        kbeauty = 0
        while j < len(str(num)):
            window = (j - i) + 1
            if window < k:
                j += 1
            elif window == k:
                num_str = str(num)
                divisor = int(num_str[i:j+1])
                if divisor != 0 and num % divisor == 0:
                    kbeauty += 1
                i +=1
                j +=1
        return kbeauty
        
