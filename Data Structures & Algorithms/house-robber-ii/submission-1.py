class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def helper(start: int, end: int):
            rob1, rob2 = 0, 0

            for i in range(start, end):
                newRob = max(rob1 + nums[i], rob2)
                rob1 = rob2
                rob2 = newRob
            
            return rob2
        
        return max(helper(0, len(nums) - 1), helper(1, len(nums)))