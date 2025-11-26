class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        count_s1 = [0] * 26
        count_s2 = [0] * 26
        l = 0
        for i in s1:
            count_s1[ord(i) - 97] += 1
        
        for r in range(len(s2)):
            count_s2[ord(s2[r]) - 97] += 1

            while r - l + 1 > k:
                count_s2[ord(s2[l]) - 97] -= 1
                l += 1
            
            if count_s2 == count_s1:
                return True
        return False

