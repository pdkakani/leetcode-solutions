# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        res = []
        def dfs(node):
            if not node:
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        index = 0
        preorder = data.split(",")
        
        def dfs(low, high):
            nonlocal index
            if index == len(preorder):
                return None
            val = int(preorder[index])
            if val <= low or val >= high:
                return None
            
            node = TreeNode(val)
            index += 1

            node.left = dfs(low, node.val)
            node.right = dfs(node.val, high)

            return node

        return dfs(float("-inf"), float("inf"))


        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
