# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDia = 0

        def dfs(node: Optional[TreeNode]) -> int:
            """Return the depth of the tree at the given node"""
            nonlocal maxDia

            if not node:
                return 0
            
            leftDepth = dfs(node.left)
            rightDepth = dfs(node.right)

            maxDia = max(maxDia, leftDepth + rightDepth)

            return max(1 + leftDepth, 1 + rightDepth)
        
        dfs(root)
        return maxDia
    




        