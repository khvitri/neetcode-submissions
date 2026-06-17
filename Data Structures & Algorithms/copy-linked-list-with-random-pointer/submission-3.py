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
        ogToCopy = {}
        dummyNode = Node(0)

        curr = head
        while curr:
            ogToCopy[curr] = None
            curr = curr.next
        
        curr = head
        ogToCopy[curr] = Node(curr.val) if curr else None
        dummyNode.next = ogToCopy[curr]

        while curr:
            currCopy = ogToCopy[curr] if ogToCopy[curr] else Node(curr.val)

            if curr.next:
                currCopy.next = ogToCopy[curr.next] if ogToCopy[curr.next] else Node(curr.next.val)
                ogToCopy[curr.next] = currCopy.next
            
            if curr.random:
                currCopy.random = ogToCopy[curr.random] if ogToCopy[curr.random] else Node(curr.random.val)
                ogToCopy[curr.random] = currCopy.random
            
            ogToCopy[curr] = currCopy

            curr = curr.next
 
        return dummyNode.next


