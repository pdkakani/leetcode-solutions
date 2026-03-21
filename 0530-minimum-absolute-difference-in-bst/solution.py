# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        result = float('inf')
        prev = None # tracks the previously visited node in-order

        def inorder(node):
            nonlocal result
            nonlocal prev
            if not node:
                return
            
            # go left first
            inorder(node.left)

            # visit current node
            if prev is not None:
                result = min(result, node.val - prev)
            prev = node.val # update prev to current
            
            inorder(node.right)

        inorder(root)
        return result
        
