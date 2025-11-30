# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]

        def compute_h(node):
            if not node:
                return 0
            
            l_h, r_h = compute_h(node.left), compute_h(node.right)
            

            if abs(l_h - r_h) > 1:
                balanced[0] = False
                return 0
            
            return 1 + max(l_h, r_h)
        
        compute_h(root)
        return balanced[0]
