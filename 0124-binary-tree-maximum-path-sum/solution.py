# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = float("-inf")

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            
            # in case there are negatives on the branch which negates your sum, pick 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            curr_path = node.val + left + right
            res = max(res, curr_path)

            return node.val + max(left, right)
        dfs(root)
        return res

        
