# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        total = 0

        def tilt_calc(node):
            nonlocal total
            if not node:
                return 0
            
            left = tilt_calc(node.left)
            right = tilt_calc(node.right)

            total += abs(left - right)


            return left + right + node.val
            
        tilt_calc(root)
        return total
            
        
