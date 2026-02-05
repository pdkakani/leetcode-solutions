class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # res = ""
        # strs.sort(key= len)

        # # temp stores first word
        # temp = strs[0]

        # # length of first word
        # n = len(temp)
        # flag = True
        # # loop over n times - length of first word
        # for i in range(n):
            

        #     # store the first letter
        #     letter = strs[0][i]
                
            
        #     # loop over the input arr
        #     for j in range(1, len(strs)):
                
        #         if i < len(strs[j]):

        #             # compare letter of first word with letter of every word in input arr
        #             if letter != strs[j][i]:
        #                 # if the letter is not same we break the loop and return ""
        #                 flag = False
        #                 break
            
        #     if flag:
        #         res += letter

        # return res 

        smallest = min(strs)
        n = len(smallest)
        i = 0

        while i < n:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i += 1

        return strs[0][:i]  
        
