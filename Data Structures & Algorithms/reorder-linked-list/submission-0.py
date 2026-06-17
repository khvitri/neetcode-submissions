# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        if not slow.next: return

        # Reverse linked list for everything after the midpoint (slow pointer)
        curr = slow.next
        prev = None
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        curr = head
        currRev = prev
        while curr and currRev:
            nxt = curr.next
            revNxt = currRev.next
            curr.next = currRev
            currRev.next = nxt
            curr = nxt
            currRev = revNxt







