# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        nextN = head
        prevN = None
        rHead = None
        while nextN != None:
            rHead = nextN
            temp = nextN.next
            nextN.next = prevN
            prevN = nextN
            nextN = temp

        return rHead

        
        
            

        