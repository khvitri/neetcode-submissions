# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        q = deque()
        res = []
        q.append(root)

        while q:
            currLvl = []
            nextQ = deque()
            
            while q:
                node = q.popleft()

                currLvl.append(node.val)
                if node.left: nextQ.append(node.left)
                if node.right: nextQ.append(node.right)
                        
            res.append(currLvl)
            q = nextQ
        
        return res



        