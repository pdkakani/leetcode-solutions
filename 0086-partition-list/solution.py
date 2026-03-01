# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_l = ListNode()
        dummy_g = ListNode()

        less = dummy_l #walker
        greater = dummy_g #walker

        current = head
        while current:
            if current.val >= x:
                greater.next = current

                greater = greater.next
            else:
                less.next = current
                less = less.next
            current = current.next

        greater.next = None

        less.next = dummy_g.next
        return dummy_l.next
