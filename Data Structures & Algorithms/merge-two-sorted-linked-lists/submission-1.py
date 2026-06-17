# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Two pointers pointing at the beginning of both linked list
        # Compare the two values at the pointer
        # If list1[ptr1] >= list2[ptr2], then we use list1[ptr1]
        # Otherwise we use list2[ptr2]
        # Use: At the current node, make the node's next be list1[ptr1] or list2[ptr2]
        if not list1: return list2
        if not list2: return list1

        ptr1 = list1
        ptr2 = list2

        newHead = None
        ptrCurr = None
        if ptr1.val <= ptr2.val:
            newHead = ptr1
            ptrCurr = ptr1
            ptr1 = ptr1.next
        else:
            newHead = ptr2
            ptrCurr = ptr2
            ptr2 = ptr2.next

        while ptr1 or ptr2:
            print(ptr1.val if ptr1 else "bruh")
            print(ptr2.val if ptr2 else "bruh")
            print(ptrCurr.val)
            print()

            if not ptr1:
                ptrCurr.next = ptr2
                break
            elif not ptr2:
                ptrCurr.next = ptr1
                break
            elif ptr1.val <= ptr2.val:
                ptrCurr.next = ptr1
                ptrCurr = ptrCurr.next
                ptr1 = ptr1.next
            else:
                ptrCurr.next = ptr2
                ptrCurr = ptrCurr.next
                ptr2 = ptr2.next
        
        return newHead
                
            

            


