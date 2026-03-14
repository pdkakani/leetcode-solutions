# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        def helper(node):
            nonlocal max_sum

            if not node:
                return 0

            left_path_max_sum = max(0, helper(node.left))
            right_path_max_sum = max(0, helper(node.right))

            path_sum = node.val + left_path_max_sum + right_path_max_sum
            max_sum = max(max_sum, path_sum)

            return node.val + max(left_path_max_sum, right_path_max_sum)
        
        helper(root)

        return max_sum
        
