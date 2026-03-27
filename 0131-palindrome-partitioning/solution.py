class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result, path = [],[]
        def is_palindrome(inp):
            return inp[::-1] == inp

        def bt(start):
            if start == len(s):
                result.append(list(path))
                return
            
            for i in range(start, len(s)):
                subs = s[start:i+1]
                if is_palindrome(subs):
                    path.append(subs)
                    bt(i+1)
                    path.pop()
                
        bt(0)
        return result

        
