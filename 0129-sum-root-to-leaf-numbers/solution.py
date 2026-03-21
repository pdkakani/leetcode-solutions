# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0

        def dfs(node, num):
            nonlocal total
            if not node:
                return None
            
            num += (str(node.val))
            
            if not node.left and not node.right:
                total += int(num)
                return total
            
            dfs(node.left, num)
            dfs(node.right, num)

            return None
        dfs(root, "")
        return total
            
            
            
        
