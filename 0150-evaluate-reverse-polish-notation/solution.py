class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {"+", "-", "*", "/"}
        stk = []

        for i in tokens:
            if i.lstrip("-").isdigit():
                stk.append(i)
            elif i in op and stk:
                first_num = stk.pop()
                sec_num = stk.pop()
                temp = sec_num + i + first_num
                stk.append(str(int(eval(temp))))

        return int(stk[0])


