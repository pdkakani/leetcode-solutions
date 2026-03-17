# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 0
        def inorder(node):
            nonlocal counter
            if not node:
                return
            
            left = inorder(node.left)
            if left is not None:
                return left
            counter += 1

            if counter == k:
                return node.val

            right = inorder(node.right)
            if right is not None:
                return right
            
            return None
        
        return inorder(root)


        
