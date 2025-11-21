# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n

        if n == 1:
            return n

        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid) == True:
                right = mid
            elif isBadVersion(mid) == False:
                left = mid + 1
        
        return left 

