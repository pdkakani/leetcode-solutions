# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diam = [0]
        def compute_h(node):
            if not node:
                return 0
            
            l_h, r_h = compute_h(node.left), compute_h(node.right)
            diami = l_h + r_h
            diam[0] = max(diam[0], diami)
            return 1 + max(l_h, r_h)
        compute_h(root)
        return diam[0]
