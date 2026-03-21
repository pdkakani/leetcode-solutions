class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1

        carry = 0
        ans = []

        while i >=0 or j >=0 or carry:
            # a = int(num1[i]) if i >= 0 else 0
            # b = int(num2[j]) if j >= 0 else 0
            
            a = ord(num1[i]) - ord('0') if i >= 0 else 0
            b = ord(num2[j]) - ord('0') if j >= 0 else 0

            carry, digit = divmod(a + b + carry, 10)
            ans.append(str(digit))
            i-=1
            j-=1

        return ''.join(reversed(ans))
        
