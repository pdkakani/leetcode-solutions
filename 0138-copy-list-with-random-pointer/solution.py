"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mhash = {None:None}
        cur = head

        while cur:
            mhash[cur]= Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            copy = mhash[cur]
            copy.next = mhash[cur.next]
            copy.random = mhash[cur.random]
            cur = cur.next

        return mhash[head]

