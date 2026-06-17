class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums: return -1

        slow, fast = nums[0], nums[0]
        while slow != fast or slow == nums[0]:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break
        
        x = slow
        print(x)
        #        F
        # <-------------->
        # o -> o -> o -> o -> o -> o
        #                |         |
        #                o         o
        #                |         |
        #                o <- o <- o
        #
        # C = length of cycle
        # If slow traveled by F, fast would have travelled 2F
        # Fast travelled F distance within the cycle by the time slow travelled by F
        # Every time slow enters the cycle, fast would be at F mod C in the cycle
        # Fast is C - (F mod C) away from the slow pointer
        # The point of intersection for fast and slow pointer is also C - (F mod C)
        # C - (C - (F mod C)) = F mod C

        slow = nums[0]
        while x != slow:
            x = nums[x]
            slow = nums[slow]
        
        return slow
