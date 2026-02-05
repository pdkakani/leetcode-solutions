class Solution:
    def reverseWords(self, s: str) -> str:
       inpArr = s.split()
       inpArr.reverse() # positional reverse

       return " ".join(inpArr) 
        
