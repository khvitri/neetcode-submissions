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
        # Wo/ random, deepcopy of Node:
        #   1. Create new node
        #   2. new node val = current node val
        #   3. new node next = deepcopy of current node next
        # W/ random, deepcopy of Node:
        #   1. Create a dictionary: Original Node -> Deepcopy Node
        #   2. Check if current node in dictionary. If yes:
        #       a. Get existing deepcopy node via dictionary[current node]
        #       b. Perform deepcopy on current node's next and random by repeating step 2
        #   3. If no:
        #       a. Create a new node
        #       b. new node val = current node val
        #       c. Add newly created node into the dictionary[current node] = deepcopy node
        #       c. new node next = deepcopy of current node next
        #       d. new node random = deepcopy of current node random

        deepCopyDict = dict()
        curr = head
        while curr:
            deepCopyDict[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            deepCopyDict[curr].next = deepCopyDict.get(curr.next, None)
            deepCopyDict[curr].random = deepCopyDict.get(curr.random, None)
            curr = curr.next
        
        return deepCopyDict.get(head, None)


        