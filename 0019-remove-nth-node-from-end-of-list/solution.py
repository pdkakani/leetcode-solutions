# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # def get_length(head):
        #     current = head
        #     length = 0
        #     while current:
        #         length += 1
        #         current = current.next
        #     return length + 1

        # dummy = ListNode()
        # dummy.next = head

        # prev = dummy
        # current = head

        # leng = 1
        # pos = get_length(head) - n
        
        # while current:
        #     if leng == pos:
        #         prev.next = current.next
        #         break
        #     prev = current
        #     current= current.next
        #     leng += 1
        
        # return dummy.next

        dummy = ListNode()
        dummy.next = head

        fast = dummy
        slow = dummy

        for _ in range(n+1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next
        
        # slow is now at the node before the node to delete
        slow.next = slow.next.next
        return dummy.next


            

