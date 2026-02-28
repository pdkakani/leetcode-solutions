# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        tail = head
        leng = 1
        while tail.next:
            tail = tail.next
            leng += 1
        
        k = k % leng
        if k == 0:
            return head

        #make circular
        tail.next = head

        # new tail is at position leng - k - 1 from head
        new_tail = head
        for _ in range(leng - k - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None

        return new_head
