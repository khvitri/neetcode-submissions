class Solution:
    def rob(self, nums: List[int]) -> int:
        maxAfterNeighbor = 0
        maxStolen = [0] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            if i + 2 < len(nums):
                maxAfterNeighbor = max(maxAfterNeighbor, maxStolen[i + 2])
            
            maxStolen[i] = nums[i] + maxAfterNeighbor
        
        return max(maxStolen)

