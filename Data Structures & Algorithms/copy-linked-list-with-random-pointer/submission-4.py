"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ogToCopy = {None: None}

        curr = head
        while curr:
            ogToCopy[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            copy = ogToCopy[curr]
            copy.next = ogToCopy[curr.next]
            copy.random = ogToCopy[curr.random]
            curr = curr.next
        
        return ogToCopy[head]
        
