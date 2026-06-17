class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIdx = {}
        for i in range(len(nums)):
            if target - nums[i] in numToIdx:
                return [numToIdx[target - nums[i]], i]
            
            if nums[i] not in numToIdx:
                numToIdx[nums[i]] = i
        
        return [-1, -1]
