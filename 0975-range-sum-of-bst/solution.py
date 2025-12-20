# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        
        # if current node is too small, ignre left subtree
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        
        # if current node is too large, ignore right subtree
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)

        #Current node is in range, check both subtrees
        return (root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high))

        return total
