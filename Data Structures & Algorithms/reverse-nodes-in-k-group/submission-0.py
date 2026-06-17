# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy # Current reverse list
        newHead = None

        left, right = head, head
        count = 0
        while right:
            count += 1                        

            if count == k:
                count = 0
                nxt = right.next
                right.next = None
                right = nxt
                revHead = self.reverseList(left)
                newHead = revHead if not newHead else newHead

                curr.next = revHead
                curr = left
                left = right
            else:
                right = right.next
        
        if count > 0:
            curr.next = left
        
        return dummy.next
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev

