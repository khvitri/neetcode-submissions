class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        numsTotal = sum(nums)
        if numsTotal % 2 != 0: return False

        target = numsTotal // 2 
        totals = {0}

        for num in nums:
            temp = set()
            for t in totals:
                temp.add(t)
                temp.add(num + t)
            
            totals = temp

            if target in totals:
                return True
        
        return False
            