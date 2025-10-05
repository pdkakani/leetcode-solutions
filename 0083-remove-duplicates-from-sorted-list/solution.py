# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        a = head
        while a and a.next:
            if a.val == a.next.val:
                a.next = a.next.next
            else:
                a = a.next
            
        return head
        
