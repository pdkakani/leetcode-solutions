class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            while stack and stack[-1] > i:
                if k > 0:
                    stack.pop()
                    k -= 1
                else:
                    break
            stack.append(i)

        stack = stack[:len(stack) - k]
        res = "".join(stack)
        
        return res.lstrip("0") or "0"

            
        
