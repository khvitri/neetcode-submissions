# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxNode = 0

        stack = [[root, 1]]
        currNode = 1

        while stack:
            node = stack.pop()[0]

            if node:
                maxNode = max(currNode, maxNode)

                currNode += 1 
                stack.append([node.right, currNode])
                stack.append([node.left, currNode])
                continue
            
            currNode = stack[-1][1] if stack else -1
        
        return maxNode