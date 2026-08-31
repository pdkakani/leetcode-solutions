class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
            else:
                # first make the chars substr
                substr = ""
                while stack and stack[-1] != "[":
                    substr = stack.pop() + substr
                # this is popping off that opening [
                stack.pop()

                # the make the multiplier substr
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                stack.append(int(k) * substr)
        
        return "".join(stack)

        
