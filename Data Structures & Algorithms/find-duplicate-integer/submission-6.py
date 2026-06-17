class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while slow != fast or slow == 0:
            slow = nums[slow]
            fast = nums[nums[fast]]    
        
        x = slow
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

        slow = 0
        while x != slow:
            x = nums[x]
            slow = nums[slow]
        
        return slow
