class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        result = 0
        sign = 1

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-":
                result += num * sign
                num = 0
                sign = -1 if c == "-" else 1
            elif c == "(":
                stack.append(result)
                stack.append(sign)

                result = 0
                sign = 1
            elif c == ")":
                result += num * sign

                
                result *= stack.pop()
                result += stack.pop()
                num = 0
        return result + sign * num
