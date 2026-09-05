class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        numsTotal = sum(nums)
        if numsTotal % 2 != 0: return False

        target = numsTotal // 2 
        totals = {0}

        for num in nums:
            temp = set()
            for t in totals:
                if t == target:
                    return True
                
                if num + t == target:
                    return True
                
                temp.add(num + t)
            
            totals.update(temp)
        
        return False
            