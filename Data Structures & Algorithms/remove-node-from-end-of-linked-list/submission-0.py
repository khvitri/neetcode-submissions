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

        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        
        idx, removeIdx = 1, length - n + 1
        prev, curr = None, head
        while curr:
            if idx == removeIdx:
                break
            prev = curr
            curr = curr.next
            idx += 1
        
        if prev:
            prev.next = curr.next
            return head
        
        return curr.next

