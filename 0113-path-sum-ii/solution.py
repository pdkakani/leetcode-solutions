# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def helper(node, target, path):
            if not node:
                return []
            if not node.left and not node.right and target == node.val:
                res.append(path + [node.val])
            
            left = helper(node.left, target - node.val, path + [node.val])
            right = helper(node.right, target - node.val, path + [node.val])


        helper(root, targetSum, [])
        return res


        
