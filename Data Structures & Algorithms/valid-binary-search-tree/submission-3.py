# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValidBSTHelper(node: Optional[TreeNode], lower: int, upper: int) -> bool:
            if not node: return True

            if node.val > lower and node.val < upper:
                return isValidBSTHelper(node.left, lower, node.val) and isValidBSTHelper(node.right, node.val, upper)
            
            return False

        return isValidBSTHelper(root, float('-inf'), float('inf'))
