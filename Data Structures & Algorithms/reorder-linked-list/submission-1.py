# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next
        
        secondIdx = math.ceil(length / 2)
        
        secondHead = None
        curr = head
        idx = 0
        while curr:
            if idx == secondIdx:
                secondHead = curr
                break
            idx += 1
            curr = curr.next

        prev = None 
        curr = secondHead
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt     
        
        curr2 = prev
        curr1 = head
        while curr2:
            nxt1 = curr1.next
            nxt2 = curr2.next
            curr1.next = curr2
            curr2.next = nxt1
            curr1 = nxt1
            curr2 = nxt2
        
        if curr1:
            curr1.next = None
        

            