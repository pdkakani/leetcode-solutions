class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def square_sum(n):
            total = 0
            while n > 0:
                digit = n % 10
                total += digit ** 2
                n //= 10
            return total
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = square_sum(n)

        return n == 1
        
