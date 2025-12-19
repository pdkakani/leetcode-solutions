# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def helper(root, curr, target) -> bool:
            if not root:
                return False
    
            curr += root.val
            if not root.left and not root.right:
                return curr == target
            
            return (helper(root.left, curr, target) or helper(root.right, curr, target))
        
        return helper(root, 0, targetSum)
        
