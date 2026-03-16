# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()

        def helper(node):
            if not node:
                return False
            
            if k - node.val in seen:
                return True
            
            seen.add(node.val)

            left= helper(node.left)
            right = helper(node.right)
            return left or right
        return helper(root)
