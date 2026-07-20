# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, max_seen_so_far):
            nonlocal count
            if not node:
                return
            
            if node.val >= max_seen_so_far:
                count += 1

            max_seen_so_far = max(max_seen_so_far, node.val)

            left = dfs(node.left, max_seen_so_far)
            right = dfs(node.right, max_seen_so_far)
            return left or right

        dfs(root, float("-inf")) # incase the tree has negative values
        return count

        
