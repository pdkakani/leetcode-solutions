# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def helper(root, curr_sum, tsum):
            if not root:
                return False

            curr_sum += root.val

            if not root.left and not root.right:
                return curr_sum == tsum

            left = helper(root.left, curr_sum, tsum)
            right = helper(root.right, curr_sum, tsum)

            return left or right

        return helper(root, 0, targetSum)        
