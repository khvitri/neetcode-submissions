class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, count = 0, 0
        for num in nums:
            if num:
                count += 1
            else:
                res = max(res, count)
                count = 0
        
        return max(res, count)
        