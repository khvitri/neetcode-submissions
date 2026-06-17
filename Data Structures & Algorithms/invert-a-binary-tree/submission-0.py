# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Depth-first approach
        # Invert left-side first, all the way down. Then over to the right-side, all the way down.
        # Use stack to track nodes that haven't been inverted

        stack = [root]

        while stack:
            node = stack.pop()
            
            if node:
                tmp = node.left
                node.left = node.right
                node.right = tmp

                stack.append(node.right)
                stack.append(node.left)
            
        return root