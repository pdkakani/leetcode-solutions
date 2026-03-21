# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    # def __init__(self, root: Optional[TreeNode]):
    #     self.pointer = -1
    #     self.res = []
    #     self.inorder(root)
    
    # def inorder(self,node):
    #     stack = []
        
    #     curr = node
    #     while stack or curr:
    #         while curr:
    #             stack.append(curr)
    #             curr = curr.left
    #         curr = stack.pop()
    #         self.res.append(curr.val)
    #         curr = curr.right

        

    # def next(self) -> int:
    #     self.pointer += 1
    #     return self.res[self.pointer]

        

    # def hasNext(self) -> bool:
    #     n = len(self.res)
    #     return self.pointer < n - 1

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        curr = root
        while curr: 
            self.stack.append(curr)
            curr = curr.left
    

    def next(self) -> int:
        node_to_process = self.stack.pop()
        res = node_to_process.val
        node_to_process = node_to_process.right
        while node_to_process:
            self.stack.append(node_to_process)
            node_to_process = node_to_process.left
            
        return res
        

    def hasNext(self) -> bool:
        return len(self.stack) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
