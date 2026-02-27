# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # add first element of l1 to l2
        # if its less than < 10, pick the right most digit and add to l3
        # the remaning left digit should be added to the next sum
        # at last the remaining left digit should also be added to the result

        dummy = curr = ListNode()
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10

            curr.next = ListNode(digit)
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next



        # l1s = ""
        # l2s = ""
        # curr_l1 = l1
        # while curr_l1:
        #     l1s += str(curr_l1.val)
        #     curr_l1 = curr_l1.next
        
        # curr_l2 = l2
        # while curr_l2:
        #     l2s += str(curr_l2.val)
        #     curr_l2 = curr_l2.next
        
        # rev_l1 = l1s[::-1]
        # rev_l2 = l2s[::-1]
        # res = int(rev_l1) + int(rev_l2)

        # res_l = str(res)[::-1]
        # cur = dummy = ListNode()
        

        # for i in res_l:
        #     cur.next = ListNode(val=int(i))
        #     cur = cur.next
        # return dummy.next        
