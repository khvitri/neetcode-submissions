# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Find the length linked list
        # length - n + 1 (index in linked list to remove)
        # Remove length - n + 1 th node
        # If the removed node is a head, then we return a new head

        dummy = ListNode(0, head) 
        left, right = dummy, head

        # Shift right pointer by n
        # D  0  1  2  3  E
        # |--|--2--|
        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        # delete
        left.next = left.next.next

        return dummy.next



