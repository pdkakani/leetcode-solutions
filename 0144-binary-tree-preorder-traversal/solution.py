# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # result = []
        # def dfs(node):
        #     if not node:
        #         return
        #     result.append(node.val)
        #     dfs(node.left)
        #     dfs(node.right)
            
        # dfs(root)
        # return result
        if not root:
            return []
        stack = [root]
        res = []

        while stack:
            curr = stack.pop()
            
            res.append(curr.val)
            if curr.right is not None:
                stack.append(curr.right)
            if curr.left is not None:
                stack.append(curr.left)
            
        return res
        



        
