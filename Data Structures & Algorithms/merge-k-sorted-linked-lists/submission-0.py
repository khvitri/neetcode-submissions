# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # For each Linked List, it will have it's current pointer.
        # Each current pointer will be pointing to the head of its assinged linked list.
        # Get the minimum number out of the Linked List where the current pointer is pointing to.
        # Assign that minimum number to be the next of the result Linked List.
        # Shift the current pointer of that minimum number to the next part.
        # Continue until all Linked List are traversed.

        dummy = ListNode()
        curr = dummy

        while any(lists):
            minNum = ListNode(float('inf'))
            minIdx = 0

            # Remove None
            i = 0
            while i < len(lists):
                if not lists[i]:
                    lists.pop(i)
                    continue
                i += 1 

            # Find min. number
            for idx, ll in enumerate(lists):
                if minNum.val > ll.val:
                    minNum = ll
                    minIdx = idx
            
            curr.next = minNum
            curr = curr.next
            lists[minIdx] = minNum.next
        
        return dummy.next

                

                
