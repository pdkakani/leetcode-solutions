# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev_g = dummy

        while True:
            kth = prev_g

            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            
            group_n = kth.next
            prev, curr = group_n, prev_g.next

            while curr != group_n:
                next_n = curr.next
                curr.next = prev
                prev= curr
                curr = next_n
            
            temp = prev_g.next
            prev_g.next = kth
            prev_g = temp

