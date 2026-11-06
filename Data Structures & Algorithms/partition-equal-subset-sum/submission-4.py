class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False
        
        def dfs(index, target):
            if target == 0:
                return True
            
            if target < 0 or index >= len(nums):
                return False

            # Include current number or not
            if (dfs(index + 1, target - nums[index]) or
                dfs(index + 1, target)):
                return True

            return False
        
        return dfs(0, total // 2)
            

            