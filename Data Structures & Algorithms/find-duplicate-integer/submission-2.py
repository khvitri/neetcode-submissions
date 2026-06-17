class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while nums[slow] != nums[fast] or slow == 0:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        interx = slow
        slow = 0

        while nums[slow] != nums[interx]:
            slow = nums[slow]
            interx = nums[interx]
        
        return nums[slow]


        
