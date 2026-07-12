# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Get a count
        count = 0
        curr = head
        while curr:
            curr = curr.next
            count += 1
        
        mid = count // 2        
        curr = head
        for i in range(mid):
            curr = curr.next
        
        return curr
        