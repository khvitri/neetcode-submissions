# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stackP, stackQ = [p], [q]

        while stackP and stackQ:
            nodeP, nodeQ = stackP.pop(), stackQ.pop()

            if nodeP and nodeQ and nodeP.val == nodeQ.val:
                stackP.append(nodeP.right)
                stackP.append(nodeP.left)

                stackQ.append(nodeQ.right)
                stackQ.append(nodeQ.left)
                continue
            elif not nodeP and not nodeQ:
                continue
            
            return False
        
        return stackP == stackQ