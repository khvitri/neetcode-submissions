# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxSum = float('-inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def maxPathSumHelper(root: Optional[TreeNode]) -> int:
            if not root: return 0
    
            leftMaxSum = maxPathSumHelper(root.left)
            rightMaxSum = maxPathSumHelper(root.right)
    
            currMaxSum = root.val
    
            if leftMaxSum > 0: currMaxSum += leftMaxSum
            if rightMaxSum > 0: currMaxSum += rightMaxSum
    
            self.maxSum = max(self.maxSum, currMaxSum)
    
            return max(root.val, max(root.val + leftMaxSum, root.val + rightMaxSum))
        
        maxPathSumHelper(root)
        
        return self.maxSum