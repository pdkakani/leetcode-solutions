# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index_map = {v:i for i, v in enumerate(inorder)}

        def dfs(post_l, in_l, in_r):
            if in_l > in_r:
                return None
            root_val = postorder[post_l]
            root = TreeNode(root_val)

            mid = index_map[root_val]

            right_size = in_r - mid

            root.right = dfs(post_l -1, mid + 1, in_r)
            root.left = dfs(post_l - 1 - right_size, in_l, mid - 1)

            return root
        return dfs(len(postorder)-1, 0, len(inorder)-1)
        
