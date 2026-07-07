"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    oldToNew = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        if node in self.oldToNew: return self.oldToNew[node]

        newNode = Node(node.val)
        self.oldToNew[node] = newNode
        for neighbor in node.neighbors:
            newNode.neighbors.append(self.cloneGraph(neighbor))
        
        return newNode