# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode], curr_num: int = 0) -> int:
        if not root:
            return 0
        
        # Build current number
        curr_num = curr_num * 2 + root.val

        #If leaf, return the number
        if not root.left and not root.right:
            return curr_num
        
        #sum both subtrees
        return (self.sumRootToLeaf(root.left, curr_num) + self.sumRootToLeaf(root.right, curr_num))

        
