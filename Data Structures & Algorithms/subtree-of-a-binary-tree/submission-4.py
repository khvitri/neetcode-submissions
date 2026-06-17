# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sameTree(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
            """Given the two nodes, node1 is equal to node2 if they have the same values
                and all of their descendent's values are the same.
            """
            if not node1 and not node2:
                return True
            elif (node1 and node2) and node1.val == node2.val:
                return self.sameTree(node1.left, node2.left) and self.sameTree(node1.right, node2.right)

            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False

        if self.sameTree(root, subRoot): return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


        
