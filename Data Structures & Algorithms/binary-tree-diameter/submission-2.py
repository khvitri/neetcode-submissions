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
            nonlocal maxDia

            if not node:
                return 0
            
            depthL = dfs(node.left)
            depthR = dfs(node.right)

            maxDia = max(maxDia, depthL + depthR)

            return max(1 + depthL, 1 + depthR)

        dfs(root)        
        return maxDia
    




        