class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in "({[":
                stack.append(char)
            elif char in mapping and stack and stack[-1] == mapping[char]:
                stack.pop()
            else:
                return False
        return len(stack) == 0
