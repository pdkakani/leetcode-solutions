class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(l, r, s):
            if len(s) == n * 2:
                res.append(s)
                return
            
            if l < n:
                helper(l + 1, r, s + '(')
            
            if r < l:
                helper(l, r + 1, s + ')')
            
        helper(0,0,'')
        return res
        
