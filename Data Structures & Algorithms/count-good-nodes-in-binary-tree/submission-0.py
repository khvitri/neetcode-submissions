# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def countGoodNodes(node: Optional[TreeNode], maxVal: int) -> int:
            if not node:
                return 0
            
            newMaxVal = max(node.val, maxVal)
            goodDes = countGoodNodes(node.left, newMaxVal) + countGoodNodes(node.right, newMaxVal)

            if node.val >= maxVal:
                return 1 + goodDes
            
            return goodDes
        
        return countGoodNodes(root, float('-inf'))