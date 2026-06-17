# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        
        def dfsHeight(node: Optional[TreeNode]) -> int:
            """
            Given a node, find its height and return it. If left height differ by right height
            is more than 1, return -1.
            """
            if not node:
                return 0
            
            lHeight = dfsHeight(node.left)
            rHeight = dfsHeight(node.right)

            nonlocal balanced
            if not balanced:
                return 0

            if abs(lHeight - rHeight) > 1:
                balanced = False
            
            return 1 + max(lHeight, rHeight)
        
        dfsHeight(root)
        return balanced


