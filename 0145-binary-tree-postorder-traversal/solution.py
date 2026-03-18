# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # result = []

        # def dfs(node):
        #     if not node:
        #         return
            
        #     dfs(node.left)
        #     dfs(node.right)
        #     result.append(node.val)

        # dfs(root)
        # return result
        if not root:
            return []
        res = []

        stack = []
        curr = root
        last = None
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                peek = stack[-1]
                if peek.right and peek.right != last:
                    curr = peek.right
                else:
                    temp = stack.pop()
                    res.append(temp.val)
                    last = temp
                    curr = None        
            
        return res

        
