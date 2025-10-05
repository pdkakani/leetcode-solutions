# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a = list1
        b = list2
        dummy = ListNode(0)
        current = dummy

        while a and b:
            if a.val < b.val:
                current.next = a
                current = a
                a = a.next
            else:
                current.next = b
                current = b
                b = b.next
                
        current.next = a if a else b
        return dummy.next 
            
