# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    # Given a head of a linked list, reverse it and return the new head
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #       P    C    N     
        # Na <- 0 <- 1 x> 2 -> 3 -> NA

        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev



        
        
            

        