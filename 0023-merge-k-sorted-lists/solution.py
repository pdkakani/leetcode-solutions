# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        result = lists[0]
        # logic should grab first list and merge with 2 list 
        # point current to result merge list
        # use the merged list to merge with 3rd list and so on 
        def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            
            dummy = ListNode()
            current = dummy

            a = list1
            b = list2

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

        
        for i in range(1, len(lists)):
            result = mergeTwoLists(self, result, lists[i])
        
        return result

