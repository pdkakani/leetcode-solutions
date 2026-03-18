# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        prev = None
        def inorder(node):
            nonlocal prev
            if not node:
                return True
            
            left = inorder(node.left)
            if not left:
                return False

            if prev is not None: 
                if prev >= node.val:
                    return False
            prev = node.val

            right = inorder(node.right)

            if not right:
                return False

            return True
        return inorder(root)
