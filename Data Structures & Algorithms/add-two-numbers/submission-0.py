# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # carry = 0
        # lSum = ListNode()
        # while l1[ptr1] and l2[ptr2] not null:
        #   total = l1[ptr1] + l2[ptr2] + carry
        #   if total >= 10: 
        #       total, carry = total - 10, 1
        #   else: 
        #       carry = 0
        #   lSum.next = ListNode(total, None)
        #   lSum = lSum.next
        #   ptr1 += 1
        #   ptr2 += 1
        # while carry:
        #   if l1:
        #       total = l1[ptr1] + carry
        #       if total >= 10 
        #           total, carry = total - 10, 1
        #       else: 
        #           carry = 0
        #       ptr1 += 1
        #       lSum.next = ListNode(total, None)
        #   elif l2:
        #       total = l2[ptr2] + carry
        #       if total >= 10 
        #           total, carry = total - 10, 1
        #       else: 
        #           carry = 0
        #       ptr2 += 1
        #       lSum.next = ListNode(total, None)
        #   else:
        #       lSum.next = ListNode(carry, None)
        #       carry = 0
        #
        # return lSum.next

        carry = 0
        dummy = ListNode()
        lSum = dummy
        while l1 or l2 or carry:
            total = 0
            if l1 and l2:
                total = l1.val + l2.val + carry
                l1, l2 = l1.next, l2.next
            elif l1:
                total = l1.val + carry
                l1 = l1.next
            elif l2:
                total = l2.val + carry
                l2 = l2.next
            else:
                lSum.next = ListNode(carry, None) 
                carry = 0
                break
            
            if total >= 10:
                total, carry = total - 10, 1
            else:
                carry = 0
            
            lSum.next = ListNode(total, None)
            lSum = lSum.next

        return dummy.next

