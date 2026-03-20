# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {v:i for i,v in enumerate(inorder)}
        def dfs(pre_l, in_l, in_r):
            if in_l > in_r:
                return None
            root_val = preorder[pre_l]
            root = TreeNode(root_val)

            mid = index_map[root_val]
            left_size = mid - in_l

            root.left = dfs(pre_l + 1, in_l, mid - 1)
            root.right = dfs(pre_l + 1+ left_size, mid + 1, in_r)
            return root
        return dfs(0, 0, len(inorder) - 1)
        
