# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        

        def helper(node):
            if not node:
                return (0,0) # rob, this node, dont rob this node
            
            # Get results from children (bottom-up)
            left = helper(node.left)
            right = helper(node.right)

            #choice 1: Rob current Node
            # Cant rob children, so take thier "not robbed" values
            rob_current = node.val + left[1] + right[1]

            #Choice 2: Dont rob current node
            # Can can max of rob and dont rob
            not_rob_current = max(left) + max(right)

            return (rob_current, not_rob_current)

        res = helper(root)
        return max(res)

        
