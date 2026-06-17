# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    # Given a head of a linked list, reverse it and return the new head
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None 

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        
        return newHead



        
        
            

        