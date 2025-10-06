# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c = head
        n = c.next

        while n:
            temp = math.gcd(c.val, n.val)
            g = ListNode(temp)
            c.next = g
            g.next = n
            c = n
            n = c.next
        return head 
