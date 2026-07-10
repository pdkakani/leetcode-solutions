class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = {}

        for c in s1:
            s1Count[c] = s1Count.get(c, 0) + 1
        
        window_count = {}
        left = 0

        for right in range(len(s2)):
            c = s2[right]
            window_count[c] = window_count.get(c, 0) + 1

            if right - left + 1 > len(s1):
                window_count[s2[left]] -= 1
                if window_count[s2[left]] == 0:
                    del window_count[s2[left]]
                left += 1


            if right - left + 1 == len(s1):
                if window_count == s1Count:
                    return True

        return False 
        
