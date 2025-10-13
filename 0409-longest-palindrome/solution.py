class Solution:
    def longestPalindrome(self, s: str) -> int:
        count_map = Counter(s)
        result = 0
        flag = False
        for k,v in count_map.items():
            if v % 2 == 1:
                flag = True
            result += (v // 2) * 2
            
        return result + 1 if flag else result
        
