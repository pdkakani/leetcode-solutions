# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        # result = lists[0]
        # logic should grab first list and merge with 2 list 
        # point current to result merge list
        # use the merged list to merge with 3rd list and so on 
        # def mergeTwoLists(l1, l2):
        #     dummy = ListNode()

        #     curr = dummy

        #     while l1 and l2:
        #         if l1.val <= l2.val:
        #             curr.next = l1
        #             l1 = l1.next
        #         else:
        #             curr.next = l2
        #             l2 = l2.next
        #         curr = curr.next

        #     curr.next = l1 or l2
        #     return dummy.next 
        
        # for i in range(1, len(lists)):
        #     result = mergeTwoLists(result, lists[i])
        
        # return result
        arr = []

        for i in range(len(lists)):
            head = lists[i]
            while head:
                arr.append(head.val)
                head = head.next
            
        heapq.heapify(arr)
        dummy = ListNode()
        curr = dummy

        for i in range(len(arr)):
            num = heapq.heappop(arr)
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next






