# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # first find the middle
        # reverse the second half
        # then connect both heads and then both elements after head and so on
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            next_n = curr.next
            curr.next = prev
            prev = curr
            curr = next_n

        l1 = head
        l2 = prev

        while l2:
            l1_n = l1.next #save
            l2_n = l2.next #save

            l1.next = l2 # first point to second
            l2.next = l1_n # second points to next first

            l1 = l1_n #move ahead
            l2 = l2_n #move ahead

        
