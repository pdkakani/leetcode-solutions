# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(node):
            if not node:
                return (True, 0)
            
            left_balance, left_height = helper(node.left)
            right_balance, right_height = helper(node.right)
            
            height = 1 + max(left_height, right_height)
            balance = left_balance and right_balance and (abs(left_height - right_height) <= 1)
            
            return (balance, height)
        return helper(root)[0]
        

