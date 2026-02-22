class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
        stack = []


        for t in tokens:
            if not stack or t not in op:
                stack.append(int(t))
                continue
            oper = op[t]

            second = stack.pop()
            first = stack.pop()

            res = oper(first, second)
            stack.append(int(res))

        return stack[-1]

        
