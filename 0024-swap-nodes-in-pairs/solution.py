# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = dummy

        while curr.next and curr.next.next:
            node1 = curr.next
            node2 = curr.next.next

            node1.next = node2.next # node1 points to the rest
            curr.next = node2 # curr points to node2
            node2.next = node1 # node2 points to node1

            curr = curr.next.next # move forward by 2
        return dummy.next
