# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        #need access to left - 1 node and right - left + 1 node and then reverse both

        left_node = dummy
        for _ in range(left - 1):
            left_node = left_node.next
        
        prev = None
        current = left_node.next

        for _ in range(right - left + 1):
            next_node = current.next # save the next node before we break the link
            current.next = prev # reserve the pointer
            prev = current # move prev forward
            current = next_node # move current forward
       

        left_node.next.next = current
        left_node.next = prev

        return dummy.next





