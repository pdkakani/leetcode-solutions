from itertools import combinations
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
         "7": "pqrs", "8": "tuv", "9": "wxyz"}
        # n = len(digits)
        # temp =""
        # for d in digits:
        #     temp += d_map[int(d)]
        # return [''.join(c) for c in combinations(temp, n)]

        
        res,path = [],[]
        
        #index = which digit you are on
        def bt(index): 
            #used all digits, reached end
            if index == len(digits):
                res.append(''.join(path))
                return
            
            #iterate over letter in current digits group
            for letter in d_map[digits[index]]:
                path.append(letter)
                #move to next digit
                bt(index+1)
                path.pop()
        
        bt(0)
        return res



        
            
