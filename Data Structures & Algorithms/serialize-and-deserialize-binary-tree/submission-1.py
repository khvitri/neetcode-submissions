# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
        # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ''
    
        if not root: return res
    
        q = deque()
        q.append(root)
        
        while q:
            node = q.popleft()
    
            if node:
                res = res + f"{node.val}$"
                q.append(node.left)
                q.append(node.right)
            else:
                res = res + "$"

        return res
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "": return None
        
        binTreeArr = data.split("$")

        idx = 0
        q = deque()
        root = TreeNode(int(binTreeArr[0]))
        q.append(root)

        while idx < len(binTreeArr) and q:
            node = q.popleft()

            if node:
                idx += 1
                if idx >= len(binTreeArr): break
                node.left = TreeNode(int(binTreeArr[idx])) if binTreeArr[idx] else None
                q.append(node.left)

            if node:
                idx += 1
                if idx >= len(binTreeArr): break
                node.right = TreeNode(int(binTreeArr[idx])) if binTreeArr[idx] else None
                q.append(node.right)
            
        return root